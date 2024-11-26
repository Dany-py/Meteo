from django.shortcuts import render
from django.http import HttpResponse

def base_page (request):
    return HttpResponse("<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    <title>Document</title>
</head>
<body>
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
</body>
</html>")est, 'base.html')