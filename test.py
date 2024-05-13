"""
@media (max-width: 768px) {
    .container-main{
        font-size: 10rem;
        width:20rem;
        color:blue;
    }
}

@media (min-width: 769px) {
    .container-main  {
        font-size: 16px;
        color:red;
        width:800px;
        margin:auto;
        height:200px;
        background-color: rgba(100, 200, 255);
    }
}
@media (min-width: 769px) {
    .custom-container {
        margin-left:30px;
        width:600px;
        background-color: rgba(255, 255, 255, 0.5);
        display: none;
    }
        .st-am {
        background-color:green;
        width:600px;

    }
     h1 {
            color:#065dac;
            font-size:30px;
            text-align:center;
            margin:auto;

        }
}

"""
# Definindo o CSS com uma consulta de mídia
css = """

@media (min-width: 769px) {
    .container-main  {
        font-size: 16px;
        color:red;
        width:800px;
        margin-top:150px;
        height:400px;
        
        background-color: rgba(255, 255, 255);
        border-radius:30px;
    }
    .custom-container {
        display:none;
    }
    .container-main h5 {
        font-size:18px; 
        padding-left:40px;
            
    }
  
    .container-main ul {
        text-align:center;
    }
    .container-main li {
        display: inline-block; /* Faz com que os itens da lista fiquem em linha */
        text-align:justify;
        padding-left:80px;        
    }
  
    .stApp {
        margin:auto;
        margin-top:100px;
        width:1200px;
        
        border-radius:30px;
        background-color: rgba(255, 255, 255, 0.5);
        overflow-y: hidden;
    }
    body {
        background-color:#b6cee3;
        
    }
    /*h1 estilizado*/  
    .h1-title {
        font-family: "Source Sans Pro", sans-serif;
        font-weight: 700;
        color: rgb(49, 51, 63);
        text-align:center;
        
        
    }
    .st-am {
        width:300px;
        margin-left:100px;
        margin-bottom:30px;
        text-align:center;
    }
    .st-emotion-cache-l9bjmx p {
        /* word-break: break-word; */
        margin-bottom: 55px;
      
        /* font-size: 14px; */
}

"""

# Adicionando o CSS à página


# Exemplo de uso da classe CSS
