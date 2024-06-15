css_style = """
<style>
    .icon {
        height:35px;
        width:30px;
     
    }
    .main {
        display: flex;
        flex-direction: column;
        
        margin-top: 9px;
       
    }
    .poup-up {
        width:400px;
           
    }
    .st-emotion-cache-p5msec {
            position: relative;
            display: flex;
            width: 60%;
            font-size: 14px;
            padding: 0.75rem 1rem;
            list-style-type: 
    }
    

    .st-emotion-cache-1clstc5 {
            padding-bottom: 1rem;
            padding-left: 36%;
            
        }
    .st-emotion-cache-1dtefog {
        display: flex;
        gap: 0.5rem;
        -webkit-box-align: center;
        align-items: left;
        -webkit-box-flex: 1;
        flex-grow: 1;
        flex-direction: row-reverse;
    }
   
    .table {
    
        color: #212529;
        background-color:#0552d43b;
        width:100%;
    }
    .st-emotion-cache-uf99v8 {
      
     
        background-color: #0000005c;
    } 
    .greeting {
        font-size: 24px;
        font-weight: bold;
        color: #4CAF50;
    }
    
    .span-aviso {
        font-family: "Source Sans Pro", sans-serif;
        color:white;
        padding: 20px;
        background-color:#098aff;
        margin: 10px;
        border-radius:10px;
        width:440px;
        position: relative;
        left:35%;

    }
    .user_name {
        font-size: 20px;
        color:white;
        border-radius: 10px;
        background-color: #098aff;
        width:700px; 
        margin:auto;
        
        text-align: center;
    }
    .success-message {
        font-size: 18px;
        color: #ffffff;
        background-color: #4CAF50;
        padding: 10px;
        border-radius: 5px;
    }
    .title {
        text-align: center;
        margin: 0px;
        margin-bottom: 0px;
        font-weight: bold;
        font-size: 40px;
        color: white;


    }
    .st-emotion-cache-l9bjmx p {
        word-break: break-word;
        margin-bottom: 0px;
        font-size: 18px;
    }
    
    .st-emotion-cache-z5fcl4 {
        width: 100%;
        padding:45px 5px;
        min-width: auto;
        max-width: initial;
    }
    p {
        color:white;
        font-size:16px;
         font-weight: bold;

    }
    
    .table-responsive {
        overflow-x: hidden;
    
    }
    [data-testid="baseButton-secondary"] {
        background-color:#e63946; /* Cor de fundo */
    }
     @media only screen and (max-width: 768px) {
        .st-emotion-cache-1clstc5 {
            padding-bottom: 1rem;
            padding-left: 1%;
        }
        .user_name {
            width:300px; 
            
        }
        .span-aviso {
            font-family: "Source Sans Pro", sans-serif;
            color: white;
            padding: 20px;
            background-color: #098aff;
            margin: auto;
            border-radius: 10px;
            width: 300px;
            background-color:#098aff;
            font-size: 15px;
            position: relative;
            left: 0px;
        }
         [data-testid="baseButton-secondary"] {
            margin-right: 0;
            left: 0;
            top: 0;
            float: none;
            margin-top:10px;
            width: 100%; /* Ajusta a largura para 100% */
            box-sizing: border-box; /* Inclui o padding e border no cálculo da largura */
        }
    }
    @media (min-width: 1300px) {
    iframe {
        width: 100%;
        border-radius:12px;
        height: 550px;
        
        
    }
    [data-testid="baseButton-secondary"] {
        background-color: #e63946; /* Cor de fundo */
        padding: 20px; /* Espaçamento interno */
        margin-right:320px;
        border-radius: 10px; /* Bordas arredondadas */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Sombra */
        text-align: center; /* Centralizar texto */
        font-size: 18px; /* Tamanho da fonte */
        color: #333; /* Cor do texto */
        top:10px;
        float: right; /* Adiciona alinhamento à direita */
        position:relative;
        
        
    }
    
  
}
</style>
"""

hidden_menu = """

    <style>

        .st-emotion-cache-18ni7ap {

            height:80px;
            background:#098aff;
            display: flex;
            justify-content: space-evenly;


        }

        .link-container {
            display: flex;
            gap:100px;

        }
        .link-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-decoration: none;
            justify-content: space-evenly;
        }
        .link-item i {
            font-size: 24px;
            margin-bottom: 5px;
            color:white;
        }
        .link-item a {
            text-decoration: none;
            color: inherit;
            color:white;
        }


        #MainMenu {
            visibility: hidden;

        }
        footer {visibility: hidden;}

    </style> 
"""

prox_style = """
    <style>
    
    [data-testid="baseButton-secondary"] {
        background-color: #e63946; /* Cor de fundo */
        padding: 10px; /* Espaçamento interno */
     
        border-radius: 10px; /* Bordas arredondadas */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Sombra */
        text-align: center; /* Centralizar texto */
        font-size: 18px; /* Tamanho da fonte */
        color: #333; /* Cor do texto */
        top: 5px; /* Ajuste para aproximar do .span-aviso-prox */
        left: 150px; /* Ajuste para alinhar com .span-aviso-prox */
        float: left; /* Adiciona alinhamento à direita */
        position: relative;
    }

    .span-aviso {
        font-family: "Source Sans Pro", sans-serif;
        color: white;
        padding: 20px;
        background-color: #098aff;
        margin: auto;
        border-radius: 10px;
        width: 290px;
        font-size: 15px;
        position: relative;
        top: 50px; /* Ajuste para aproximar do .span-aviso-prox */
        left: 19%; /* Ajuste para alinhar com .span-aviso-prox */
    }

    .span-aviso-prox {
        font-family: "Source Sans Pro", sans-serif;
        color: white;
        padding: 20px;
        background-color: #74e2ba;
        margin: auto;
        border-radius: 10px;
        width: 460px;
        font-size: 20px;
        text-align: center;
        position: relative;
        top: 108px;
        right: 10%;
    }

    /* Estilos para telas menores */
    @media only screen and (max-width: 768px) {
        [data-testid="baseButton-secondary"] {
            margin-right: 0;
            left: 0;
            top: 0;
            float: none;
            width: 100%; /* Ajusta a largura para 100% */
            box-sizing: border-box; /* Inclui o padding e border no cálculo da largura */
        }

        .span-aviso {
            width: calc(100% - 40px); /* Ajusta a largura */
            left: 0;
            margin:20px;
            top: 10px; /* Ajusta a posição */
        }

        .span-aviso-prox {
            width: calc(100% - 40px); /* Ajusta a largura */
            top: 10px; /* Ajusta a posição */
            right: 0;
        }
    }
</style>

    
    
"""