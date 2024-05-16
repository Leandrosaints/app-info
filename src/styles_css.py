

custom_css = """
    <style>
        
        .custom-container {
            height:400px;
            width:370px;
            margin: 0px auto;
            border-radius: 0.5rem;
            box-shadow:  4px 0 0px 0 rgba(0, 0, 0, 0.1);
            margin-top: 0px; /* Reduz a margem superior */
        }
        
    </style>
"""

custom_main = """
    <style>
        .custom-div{
            display:none;
        
        }
        .container-main {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            padding:  0px 20px;
            width:360px;
            height:auto;
            margin-top:100px;
            background-color: rgba(255, 255, 255);
            border-radius: 0px 70px 0 0;
            box-shadow: 0  0 0 rgba(0, 0, 0, 0.1);
            
    }
        .container-main h5 {
            font-size:18px; 
            padding-left:40px;
            
    }
        .container-main h3 {
            font-size:30px;
            text-align:center;
    }   
  
       
        .container-main ul {
            
            padding: 0;
            margin: 0;  
 
           
           
        }
        .container-main li {
            display: inline-block; /* Faz com que os itens da lista fiquem em linha */
            text-align:justify;
            padding-left:80px;
        {
               

    </style>
"""



# Aplicar os estilos CSS personalizados

hidden_menu= """
    
    <style>
          
        .st-emotion-cache-18ni7ap {
           
            height:80px;
            background:#065dac;
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