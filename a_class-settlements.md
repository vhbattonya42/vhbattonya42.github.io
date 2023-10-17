---
layout: page
title: Class Settlements
---

<html>
    <head>
        <title>Class Settlements</title>
        <style>
        /* body {
            font-family: Arial, sans-serif;
            /* background-color: #F2F2F2; 
        } */
        header {
            /* background-color: #333; */
            color: #333;
        }
        header h1 {
            margin: 5;
        }
        nav {
            display: flex;
            justify-content: space-between;
        }
        nav ul {
            list-style: none;
            display: flex;
            margin: 0;
            padding: 0;
        }
        nav li {
            margin: 0 10px;
        }
        nav a {
            color: #333;
            text-decoration: none;
            /* font-weight: bold; */
        }
        .settlement-box {
            border: 3px solid black;
            padding: 10px;
            margin: 10px;
            border-radius: 10px;
        }
        h2 {
            margin-top: 0;
        }
        p {
            line-height: 0;
        }
        </style>
        <!-- <script>
            function checkPassword() {
                var password = prompt("Please enter your password:");
                if (password == "123") {
                } else {
                    alert("Incorrect password, please try again.");
                    checkPassword();
                }
            }
        </script> -->
    </head>
    <!-- <body onload="checkPassword()"> -->
    <!-- <header>
      <h1>Class Settlements</h1>
    </header> -->
    <!-- <nav>
        <ul>
        {% for settlement in site.data.settlements %}
            <li><a href="{{ settlement.link }}" target="_blank">{{ settlement.id }}</a></li>
        {% endfor %}
        </ul>
    </nav> -->
    <main>
        {% for settlement in site.data.settlements %}
        <section class="settlement-box" id="{{ settlement.id }}">
            <h2><a href="{{ settlement.link }}" target="_blank">{{ settlement.name }}</a></h2>
            <h3>Description</h3>
            <p>
                {{ settlement.description }}
            </p>
            <h3>Proof</h3>
            <p>
                {{ settlement.proof }}
            </p>
            <h3>Max Amount</h3>
            <p>${{ settlement.max_amount }} w/o Proof</p>
            <h3>Deadline</h3>
            <p>{{ settlement.deadline }}</p>
            <h3>Date Updated</h3>
            <p>{{ settlement.date_updated }}</p>
        </section>
        {% endfor %}
    </main>
</html>
