from django.shortcuts import render
from django.http import HttpResponse

def base_page (request):
    return HttpResponse("<body>
    <div class="container">
        <p>What are you doing here?<br>Click on the button to go in a secure page.</p>
        <br><br>
        <a href=""><br>Go</a>
    </div>

    <style>
        body{
            background-color: black;
            color: white;
        }
        .container{
            margin-top: 10rem;
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            align-self: flex;
            text-align: center;
        }
        a{            
            width: 10rem;
            height: 5rem;
            text-align: center;
            background-color: blue;
            color: white;
            border-radius: 20px;
            text-decoration: none;
        }
    </style>
</body>")