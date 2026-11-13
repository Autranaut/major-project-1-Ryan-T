import flet as ft
import json

account = {} #who you are signed in as
match = {} #best match for the user

def main(page: ft.Page):
    def main_page():
        page.controls.clear()
        page.title = "hot singles in your area"
        page.bgcolor = ft.Colors.BLUE_100
        page.window.width = 1200
        page.window.height = 800
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        global account

        def enter_signup(e):
            signup()

        def enter_login(e):
            login_page()

        def signout(e):
            global account
            account = {}
            main_page()

        def enter_match(e):
            match_page()

        accbar = ft.Text(size = 16, color = ft.Colors.BLUE_ACCENT)
        try:
            accbar.value = "Logged in as " + account["fname"] + " " + account["lname"]
        except:
            accbar.value = "Not logged in"

        register_btn = ft.Button(
            icon = ft.Icons.ADD,
            on_click = enter_signup
        )
        if len(account) == 0:
            register_btn.content = "Create an account"
        else:
            register_btn.content = "Edit account data"

        login_btn = ft.Button(
            content = "Sign in",
            icon = ft.Icons.DOUBLE_ARROW,
            on_click = enter_login
        )

        signout_btn = ft.Button(
            content = "Log out",
            icon = ft.Icons.EXIT_TO_APP,
            on_click = signout
        )

        match_btn = ft.Button(
            content = "Find a date",
            icon = ft.Icons.HEART_BROKEN_SHARP,
            bgcolor = ft.Colors.PINK_100,
            on_click = enter_match
        )
        if len(account) == 0:
            match_btn.disabled = True
        else:
            match_btn.disabled = False

        page.add(
            ft.Container(
                padding = 20,
                margin = 220,
                alignment = ft.Alignment.CENTER,
                bgcolor = ft.Colors.BLUE_50,
                width = 470,
                height = 360,
                border_radius = 10,
                expand = True,
                content = ft.Column(
                    controls = [
                        accbar,
                        ft.Text("Welcome!", size = 32),
                        ft.Text("Select an option below to continue", size = 24),
                        login_btn if len(account) == 0 else signout_btn,
                        register_btn,
                        match_btn
                    ]
                )
            )
        )

    def signup():
        page.controls.clear()
        page.bgcolor = ft.Colors.BLUE_100
        page.title = "attractive unmarried people in your vicinity"
        page.scroll = "auto"

        fname_input = ft.TextField(label = "First name", hint_text = "Enter first name")
        lname_input = ft.TextField(label = "Last name", hint_text = "Enter last name")
        password_input = ft.TextField(label = "Password", hint_text = "Enter password", password = True, can_reveal_password = True)
        password_conf_input = ft.TextField(label = "Confirm password", hint_text = "Confirm password", password = True, can_reveal_password = True)
        
        gender_rad = ft.RadioGroup(
            content = ft.Column([
                ft.Radio(value = "male", label = "Male"),
                ft.Radio(value = "female", label = "Female"),
                ft.Radio(value = "other", label = "Other/Prefer not to say")
            ])
        )
        
        age_input = ft.TextField(label = "Age", hint_text = "Enter age")
        
        income_rad = ft.RadioGroup(
            content = ft.Column([
                ft.Radio(value = "low", label = "$1"),
                ft.Radio(value = "high", label = "More than $1")
            ])
        )
        
        personality_rad = ft.RadioGroup(
            content = ft.Column([
                ft.Radio(value = "extr", label = "Entroverted, outgoing"),
                ft.Radio(value = "neutral", label = "Somewhere in between"),
                ft.Radio(value = "intr", label = "Introverted, keeping to yourself")
            ])
        )
        
        exercise_rad = ft.RadioGroup(
            content = ft.Column([
                ft.Radio(value = "none", label = "Less than 1 hour"),
                ft.Radio(value = "low", label = "1-3 hours"),
                ft.Radio(value = "med", label = "3-7 hours"),
                ft.Radio(value = "high", label = "7-14 hours"),
                ft.Radio(value = "vhigh", label = "More than 14 hours")
            ])
        )
        
        read_tf = ft.RadioGroup(
            content = ft.Column([
                ft.Radio(value = "true", label = "Yes"),
                ft.Radio(value = "false", label = "No")
            ])
        )
        
        hobbies_rad = ft.RadioGroup(
            content = ft.Column([
                ft.Radio(value = "paint", label = "Painting"),
                ft.Radio(value = "chat", label = "Chatting"),
                ft.Radio(value = "party", label = "Partying")
            ])
        )
        
        cheeseburger_rad = ft.RadioGroup(
            content = ft.Column([
                ft.Radio(value = "love", label = "Love of your life"),
                ft.Radio(value = "burger", label = "Cheeseburger"),
            ])
        )
        
        global account
        if len(account) != 0: #put the values back
            fname_input.value = account["fname"]
            lname_input.value = account["lname"]
            password_input.value = account["pass"]
            password_conf_input.value = account["pass"]
            gender_rad.value = account["gend"]
            age_input.value = account["age"]
            income_rad.value = account["inc"]
            personality_rad.value = account["pers"]
            exercise_rad.value = account["exer"]
            read_tf.value = account["read"]
            hobbies_rad.value = account["hobb"]
            cheeseburger_rad.value = account["cheese"]
            fname_input.read_only = True
            lname_input.read_only = True

        accbar = ft.Text(size = 16, color = ft.Colors.BLUE_ACCENT)
        try:
            accbar.value = "Logged in as " + account["fname"] + " " + account["lname"]
        except:
            accbar.value = "Not logged in"
        
        def menu_return(e):
            main_page()

        def submit(e):
            if len(fname_input.value) == 0 or len(lname_input.value) == 0 or gender_rad.value is None or len(age_input.value) == 0 or income_rad.value is None or len(personality_rad.value) == 0 or exercise_rad.value is None or read_tf.value is None or hobbies_rad.value is None or cheeseburger_rad.value is None:
                status.value = "Please answer all questions"
                status.size = 16
                status.color = ft.Colors.RED
            elif len(password_input.value) < 6:
                status.value = "Password must be at least 6 characters"
                status.size = 16
                status.color = ft.Colors.RED
            elif password_input.value != password_conf_input.value:
                status.value = "Passwords do not match"
                status.size = 16
                status.color = ft.Colors.RED
            else:
                stored = []
                with open("data.json", "r") as f:
                    stored = json.load(f)
                found = False
                for x in stored:
                    if x["fname"] == fname_input.value and x["lname"] == lname_input.value:
                        found = True
                        if len(account) > 0:
                            stored.remove(x) #remove user because they'll be recreated 10 lines from now
                        break
                if not(found and len(account) == 0):
                    data = {}
                    data["fname"] = fname_input.value
                    data["lname"] = lname_input.value
                    data["pass"] = password_input.value
                    data["gend"] = gender_rad.value
                    data["age"] = age_input.value
                    data["inc"] = income_rad.value
                    data["pers"] = personality_rad.value
                    data["exer"] = exercise_rad.value
                    data["read"] = read_tf.value
                    data["hobb"] = hobbies_rad.value
                    data["cheese"] = cheeseburger_rad.value
                    stored.append(data)
                    with open("data.json", "w") as f:
                        json.dump(stored, f)
                if found and len(account) > 0:
                    status.value = "Account data edited!"
                    status.size = 16
                    status.color = ft.Colors.GREEN
                elif found:
                    status.value = "Account with this name already exists"
                    status.size = 16
                    status.color = ft.Colors.RED
                else:
                    status.value = "Account created successfully!"
                    status.size = 16
                    status.color = ft.Colors.GREEN

        back_button = ft.Button(
            content = "Go back",
            icon = ft.Icons.SKIP_PREVIOUS,
            on_click = menu_return
        )

        status = ft.Text("", size = 1)

        submit_button = ft.Button(
            icon = ft.Icons.ADD,
            on_click = submit
        )

        if len(account) == 0:
            submit_button.content = "Create account"
        else:
            submit_button.content = "Edit info"

        prompt = ft.Text(size = 24)
        if len(account) == 0:
            prompt.value = "Answer some questions about yourself to to get started!"
        else:
            prompt.value = "Editing data"

        page.add(
            ft.Container(
                expand = True,
                padding = 20,
                margin = 150,
                alignment = ft.Alignment.TOP_CENTER,
                bgcolor = ft.Colors.BLUE_50,
                width = 700,
                height = 1620,
                border_radius = 10,
                content = ft.Column(
                    controls = [
                        accbar,
                        prompt,
                        back_button,
                        fname_input,
                        lname_input,
                        password_input,
                        password_conf_input,
                        ft.Text("Gender:", size = 18),
                        gender_rad,
                        age_input,
                        ft.Text("Enter your income (not creepy at all)", size = 18),
                        income_rad,
                        ft.Text("How would you describe your personality?", size = 18),
                        personality_rad,
                        ft.Text("How much do you exercise every week?", size = 18),
                        exercise_rad,
                        ft.Text("Do you like to read?", size = 18),
                        read_tf,
                        ft.Text("Which of these hobbies is your favourite?", size = 18),
                        hobbies_rad,
                        ft.Text("Would you rather have the love of your life or a cheeseburger?", size = 18),
                        cheeseburger_rad,
                        status,
                        submit_button
                    ]
                )
            )
        )

    def login_page():
        page.controls.clear()
        page.title = "arousing humans not presently in a romantic relationship within a reasonably small distance from you"
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.vertical_alignment = ft.MainAxisAlignment.START
        page.window.width = 1200
        page.window.height = 800
        page.bgcolor = ft.Colors.BLUE_100

        accbar = ft.Text(size = 16, color = ft.Colors.BLUE_ACCENT)
        try:
            global account
            accbar.value = "Logged in as " + account["fname"] + " " + account["lname"]
        except:
            accbar.value = "Not logged in"

        def back(e):
            main_page()

        def login_attempt(e):
            found_user = False
            exists = False
            stored_dicts = []
            with open("data.json", "r") as f:
                stored_dicts = json.load(f)
            for x in stored_dicts:
                if x["fname"] == fname_input.value and x["lname"] == lname_input.value:
                    exists = True
                    if x["pass"] == pass_input.value:
                        global account
                        account = x
                        found_user = True
                        break
            if found_user:
                status.value = "Successfully logged in as " + account["fname"] + " " + account["lname"]
                accbar.value = "Logged in as " + account["fname"] + " " + account["lname"]
                status.size = 16
                status.color = ft.Colors.GREEN
            elif exists:
                status.value = "Password is incorrect"
                status.size = 16
                status.color = ft.Colors.RED
            else:
                status.value = "No user with this name exists"
                status.size = 16
                status.color = ft.Colors.RED


        back_button = ft.Button(
            content = "Go back",
            icon = ft.Icons.SKIP_PREVIOUS,
            on_click = back
        )

        login_button = ft.Button(
            content = "Login",
            icon = ft.Icons.PLAYLIST_ADD,
            on_click = login_attempt
        )

        fname_input = ft.TextField(label = "First name", hint_text = "Enter first name")
        lname_input = ft.TextField(label = "Last name", hint_text = "Enter last name")
        pass_input = ft.TextField(label = "Password", hint_text = "Enter password", password = True, can_reveal_password = True)
        status = ft.Text("", size = 1)

        page.add(
            ft.Container(
                expand = True,
                padding = 20,
                margin = 150,
                alignment = ft.Alignment.CENTER,
                bgcolor = ft.Colors.BLUE_50,
                width = 500,
                height = 500,
                border_radius = 10,
                content = ft.Column(
                    controls = [
                        accbar,
                        ft.Text("Login", size = 42),
                        back_button,
                        fname_input,
                        lname_input,
                        pass_input,
                        status,
                        login_button
                    ]
                )
            )
        )

    def match_page():
        page.controls.clear()
        page.title = "members of a set of size two or greater of organisms belonging to the genus homo and the species sapiens, each of whom is situated as of the moment of the displaying of this text message within a distance from the physical position of you, the reader and user of this program, in space that you would deem to be acceptable by your current standards for travel, and each of whom is capable of stimulating sufficient quantities of dopamine and oxytocin in the brain of the target user so as to render the concept of engaging in potentially intimate activity or otherwise with said homo sapiens organism interesting to the user of this service, and whom are not currently engaged in such an intimate and/or romantic relationship themselves"
        page.window.width = 1200
        page.window.height = 800
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.bgcolor = ft.Colors.PINK_100

        accbar = ft.Text(size = 16, color = ft.Colors.PINK_ACCENT)
        try:
            global account
            accbar.value = "Logged in as " + account["fname"] + " " + account["lname"]
        except:
            accbar.value = "Not logged in"

        def back(e):
            main_page()
        
        def find_match(e):
            storedusers = []
            with open("data.json", "r") as f:
                storedusers = json.load(f)
            inc_diffs = { #score
                "low": 1,
                "high": 2
            }
            pers_diffs = {
                "extr": 1,
                "neutral": 1.5,
                "intr": 4
            }
            ex_diffs = {
                "none": 1,
                "low": 1.3,
                "med": 2,
                "high": 5,
                "vhigh": 7
            }
            read_diffs = {
                "true": 1,
                "false": 1.2
            }
            hobb_diffs = {
                "paint": 1,
                "chat": 1.2,
                "party": 8
            }
            cheese_diffs = {
                "love": 1,
                "burger": 1.01
            }
            bestpick = {}
            bestscore = pow(10, 500)
            for x in storedusers:
                difference = 1 #math alert
                difference *= pow(abs(int(account["age"]) - int(x["age"])), 0.6)
                if inc_diffs[account["inc"]] >= inc_diffs[x["inc"]]:
                    difference *= (inc_diffs[account["inc"]] / inc_diffs[x["inc"]])
                else:
                    difference *= (inc_diffs[x["inc"]] / inc_diffs[account["inc"]])
                if pers_diffs[account["pers"]] >= pers_diffs[x["pers"]]:
                    difference *= (pers_diffs[account["pers"]] / pers_diffs[x["pers"]])
                else:
                    difference *= (pers_diffs[x["pers"]] / pers_diffs[account["pers"]])
                if ex_diffs[account["exer"]] >= ex_diffs[x["exer"]]:
                    difference *= (ex_diffs[account["exer"]] / ex_diffs[x["exer"]])
                else:
                    difference *= (ex_diffs[x["exer"]] / ex_diffs[account["exer"]])
                if read_diffs[account["read"]] >= read_diffs[x["read"]]:
                    difference *= (read_diffs[account["read"]] / read_diffs[x["read"]])
                else:
                    difference *= (read_diffs[x["read"]] / read_diffs[account["read"]])
                if hobb_diffs[account["hobb"]] >= hobb_diffs[x["hobb"]]:
                    difference *= (hobb_diffs[account["hobb"]] / hobb_diffs[x["hobb"]])
                else:
                    difference *= (hobb_diffs[x["hobb"]] / hobb_diffs[account["hobb"]])
                if cheese_diffs[account["cheese"]] >= cheese_diffs[x["cheese"]]:
                    difference *= (cheese_diffs[account["cheese"]] / cheese_diffs[x["cheese"]])
                else:
                    difference *= (cheese_diffs[x["cheese"]] / cheese_diffs[account["cheese"]])
                if (x == storedusers[0] or difference < bestscore) and x != account:
                    bestpick = x
                    bestscore = difference
            global match
            match = bestpick
            date_page()

        back_button = ft.Button(
            content = "Go back",
            icon = ft.Icons.SKIP_PREVIOUS,
            on_click = back
        )
        
        user_count_display = ft.Text(size = 24)
        user_count: int
        with open("data.json", "r") as f:
            stored = json.load(f)
            user_count = len(stored) - 1
            user_count_display.value = str(user_count) + " potential dates waiting"

        match_button = ft.Button(
            content = "Calculate best match",
            icon = ft.Icons.INSERT_LINK,
            bgcolor = ft.Colors.PINK_100,
            on_click = find_match
        )
        if user_count < 1:
            match_button.disabled = True
        else:
            match_button.disabled = False

        state = ft.Text("Match me!", size = 80)

        page.add(
            ft.Container(
                expand = True,
                padding = 20,
                margin = 200,
                alignment = ft.Alignment.CENTER,
                bgcolor = ft.Colors.PINK_50,
                width = 500,
                height = 400,
                border_radius = 10,
                content = ft.Column(
                    controls = [
                        accbar,
                        back_button,
                        state,
                        user_count_display,
                        match_button
                    ]
                )
            )
        )

    def date_page():
        page.controls.clear()
        page.title = "p"
        page.window.width = 1200
        page.window.height = 800
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.bgcolor = ft.Colors.PINK_100

        def back(e):
            main_page()

        def view(e):
            match_info_page()
        
        accbar = ft.Text(size = 16, color = ft.Colors.PINK_ACCENT)
        try:
            global account
            accbar.value = "Logged in as " + account["fname"] + " " + account["lname"]
        except:
            accbar.value = "Not logged in"

        back_button = ft.Button(
            content = "Return to menu",
            icon = ft.Icons.SKIP_PREVIOUS,
            on_click = back
        )

        view_button = ft.Button(
            content = "View info",
            icon = ft.Icons.REMOVE_RED_EYE,
            on_click = view
        )

        matchup = ft.Text(size = 60)
        matchup.value = match["fname"] + " " + match["lname"]

        comment = ft.Text(size = 20)
        if len(match["fname"]) % 3 == 0:
            comment.value = "You two have a lot in common!"
        elif len(match["fname"]) % 3 == 1:
            comment.value = "You two go well with each other!"
        else:
            comment.value = "nice"

        status = ft.Text(size = 1, color = ft.Colors.RED)

        page.add(
            ft.Container(
                expand = True,
                padding = 20,
                margin = 190,
                alignment = ft.Alignment.CENTER,
                bgcolor = ft.Colors.PINK_50,
                width = 400,
                height = 420,
                border_radius = 10,
                content = ft.Column(
                    controls = [
                        accbar,
                        matchup,
                        ft.Text(value = "is your perfect date!", size = 32),
                        comment,
                        status,
                        view_button,
                        back_button
                    ]
                )
            )
        )

    def match_info_page():
        page.controls.clear()
        page.title = "leak your personal information simulator"
        page.window.height = 800
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.vertical_alignment = ft.MainAxisAlignment.CENTER

        global match
        date_name = ft.Text(size = 30)
        date_name.value = "Name: " + match["fname"] + " " + match["lname"]
        date_gender = ft.Text(size = 20)
        if match["gend"] == "male":
            date_gender.value = "Gender: Male"
        elif match["gend"] == "female":
            date_gender.value = "Gender: Female"
        else:
            date_gender.value = "Gender: Other/Prefer not to say"
        date_age = ft.Text(size = 20)
        date_age.value = "Age: " + match["age"]
        date_income = ft.Text(size = 16)
        if match["inc"] == "high":
            date_income.value = "Income: rich af"
        else:
            date_income.value = "Income: Low"
        date_pers = ft.Text(size = 16)
        if match["pers"] == "extr":
            date_pers.value = "Personality: Extroverted, outgoing"
        elif match["pers"] == "neutral":
            date_pers.value = "Personality: A mix of extroverted and introverted"
        else:
            date_pers.value = "Personality: Lives in parents' basement"
        date_exer = ft.Text(size = 16)
        if match["exer"] == "none":
            date_exer.value = "Exercise habits: Literally nothing"
        elif match["exer"] == "low":
            date_exer.value = "Exercise habits: Poor"
        elif match["exer"] == "med":
            date_exer.value = "Exercise habits: Average"
        elif match["exer"] == "high":
            date_exer.value = "Exercise habits: Great"
        else:
            date_exer.value = "Exercise habits: Really really good"
        date_read = ft.Text(size = 16)
        if match["read"] == "true":
            date_read.value = "Likes reading"
        else:
            date_read.value = "HATES reading with a fiery passion"
        date_hobb = ft.Text(size = 16)
        if match["hobb"] == "paint":
            date_hobb.value = "Favourite hobby: Painting"
        elif match["hobb"] == "chat":
            date_hobb.value = "Favourite hobby: Hanging out"
        else:
            date_hobb.value = "Favourite hobby: Rave partying"
        date_choice = ft.Text(size = 16)
        if match["cheese"] == "love":
            date_choice.value = "Desperate for love"
        else:
            date_choice.value = "Likes cheeseburgers"

        status = ft.Text(size = 1, color = ft.Colors.RED)
        
        def back(e):
            date_page()

        def nope(e):
            status.value = "I'm not programming that"
            status.size = 16
        
        back_button = ft.Button(
            content = "Return to previous page",
            icon = ft.Icons.SKIP_PREVIOUS,
            on_click = back
        )

        connect_button = ft.Button(
            content = "Connect!",
            icon = ft.Icons.FACE_RETOUCHING_NATURAL,
            on_click = nope
        )
        
        page.add(
            ft.Container(
                expand = True,
                padding = 20,
                margin = 125,
                alignment = ft.Alignment.TOP_LEFT,
                bgcolor = ft.Colors.PINK_50,
                width = 600,
                height = 550,
                border_radius = 10,
                content = ft.Column(
                    controls = [
                        back_button,
                        date_name,
                        date_gender,
                        date_age,
                        date_income,
                        date_pers,
                        date_exer,
                        date_read,
                        date_hobb,
                        date_choice,
                        status,
                        connect_button,
                    ]
                )
            )
        )

    main_page()

ft.run(main)