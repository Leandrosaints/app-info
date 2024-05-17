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
        height:450px;
        width:800px;
        background-color: rgba(255, 255, 255);
        border-radius:20px;
       
       
    }
    .custom-container {
        display:none;
    }
    .container-main h5 {
        font-family: "Source Sans Pro", sans-serif;
        font-weight: 600;
        color: rgb(49, 51, 63);
        padding: -2px 0px 1rem;
        margin: 0;
        text-align: center;
        display: flex;
        line-height: 1.5rem;
        flex-direction: column;
        flex-wrap: wrap;
        justify-content: space-around;
        align-content: space-around;
        
    }
    
    .container-main ul {
        text-align:center;
        
    }
    .container-main li {
        display: block;
        text-align: justify;
        position: relative;
        left: 246px;
    }
    .st-emotion-cache-z5fcl4 {
        width: 101%;
        padding: 0rem 5rem 10rem;
        min-width: auto;
        max-width: initial;
        overflow: hidden;
    }
    
    .stApp {
        margin:auto;
        margin-top:100px;
        margin-bottom:20px;
        width:1200px;
        border-radius:30px;
        background-color: rgba(255, 255, 255, 0.5);
        overflow-y: hidden;
        overflow-x: hidden;

    }
    body {
        background-color:#b6cee3;
        
        
    }
    .h1-title {
        font-family: "Source Sans Pro", sans-serif;
        font-weight: 700;
        color: rgb(49, 51, 63);
        text-align: justify;
        margin-left: 120px;
    }
    
    .st-am {
        width:300px;
        text-align:center;
        margin:0;
        padding:0;
    }
   
    .st-ae {
        margin-bottom:10px;
        font-family: "Source Sans Pro", sans-serif;
    }
    .st-bb {
        background-color: rgb(240, 242, 246);
        position: absolute;
        left: 125px;
        top: -80px;
        z-index: 1; /* Adiciona essa linha para colocar o elemento acima do container principal */
    }
    .st-emotion-cache-l9bjmx p {
        word-break: break-word;
        margin-bottom: 0px;
        font-size: 14px;
    }
    p {
        margin-left: 130px;
        padding-bottom: 80px;
    }
    .st-emotion-cache-18ni7ap {
        height:50px;
        background:#065dac;
        display: flex;
        justify-content: space-evenly;
    }
    
}

@media (max-width:320px) {
   .container-main  {
        font-size: 16px;
        color: red;
        height: 350px; /* Ajuste de altura */
        width: 290px;
        background-color: rgba(255, 255, 255);
        border-radius: 20px;
        margin: auto;
        overflow-y: scroll; /* Adicionado rolagem vertical */
        padding: 10px; /* Adicionado espaçamento interno */
        
    }
   
}
"""
