from flask import Flask, request, redirect, url_for, session, Response

app = Flask(__name__)
app.secret_key = "supersecret"
@app.route("/", methods = ["POST", "GET"])
def login():
    if "user" in session:
        return redirect(url_for("welcome"))
    else:
        if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")
            if username == "admin" and password == "123":
                session["user"] = username
                return redirect(url_for("welcome"))
            else:
                return f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Wrong Password</title>

        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}

            body {{
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                font-family: Arial, sans-serif;
                background: #f5f7fb;
                color: #171717;
            }}

            .error-box {{
                width: 380px;
                padding: 40px;
                text-align: center;
                background: white;
                border-radius: 14px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
            }}

            .icon {{
                font-size: 48px;
                margin-bottom: 16px;
            }}

            h1 {{
                font-size: 32px;
                margin-bottom: 12px;
            }}

            p {{
                color: #666;
                font-size: 17px;
                margin-bottom: 28px;
            }}

            .button {{
                display: inline-block;
                padding: 12px 24px;
                background: #171717;
                color: white;
                text-decoration: none;
                border-radius: 8px;
                transition: 0.2s;
            }}

            .button:hover {{
                transform: translateY(-2px);
                opacity: 0.85;
            }}
        </style>
    </head>

    <body>

        <main class="error-box">
            <div class="icon">⚠️</div>

            <h1>Wrong Password</h1>

            <p>The password you entered is incorrect. Please try again.</p>

            <a href="{url_for('login')}" class="button">Try Again</a>
        </main>

    </body>
    </html>
    '''
        
        return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Login</title>

        <style>
            * {
                box-sizing: border-box;
                margin: 0;
                padding: 0;
            }

            body {
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                font-family: Arial, sans-serif;
                background: #f5f7fb;
            }

            .form-container {
                width: 360px;
                padding: 32px;
                background: white;
                border-radius: 12px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
            }

            h1 {
                margin-bottom: 24px;
                text-align: center;
            }

            label {
                display: block;
                margin-bottom: 8px;
                font-weight: bold;
            }

            input {
                width: 100%;
                padding: 12px;
                margin-bottom: 18px;
                border: 1px solid #ccc;
                border-radius: 7px;
                font-size: 16px;
            }

            input[type="submit"] {
                background: #171717;
                color: white;
                border: none;
                cursor: pointer;
                margin-top: 5px;
            }

            input[type="submit"]:hover {
                opacity: 0.85;
            }
        </style>
    </head>

    <body>

        <div class="form-container">
            <h1>Login</h1>

            <form method="POST" action="">
                <label for="username">Username:</label>
                <input
                    name="username"
                    id="username"
                    type="text"
                >

                <label for="password">Password:</label>
                <input
                    name="password"
                    id="password"
                    type="password"
                >

                <input
                    type="submit"
                    value="Login"
                >
            </form>
        </div>

    </body>
    </html>'''


@app.route("/welcome")
def welcome():
    if "user" in session:
        return f''' 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome</title>

    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: Arial, sans-serif;
            background: #f5f7fb;
            color: #171717;
        }}

        .welcome {{
            text-align: center;
        }}

        h1 {{
            font-size: 56px;
            margin-bottom: 12px;
        }}

        p {{
            font-size: 18px;
            color: #666;
            margin-bottom: 28px;
        }}

        .buttons {{
            display: flex;
            justify-content: center;
            gap: 12px;
        }}

        .button {{
            display: inline-block;
            padding: 12px 24px;
            background: #171717;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            transition: 0.2s;
        }}

        .button:hover {{
            transform: translateY(-2px);
            opacity: 0.9;
        }}

        .logout {{
            background: #e5484d;
        }}
    </style>
</head>

<body>
    <main class="welcome">
        <h1>Welcome {session["user"]} 👋</h1>

        <p>We're glad you're here.</p>

        <div class="buttons">
            <a href="#" class="button">Get Started</a>
            <a href="{url_for('logout')}" class="button logout">Logout</a>
        </div>
    </main>
</body>
</html>
'''

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

