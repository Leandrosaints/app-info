""".color1 { #069bdb };
.color2 { #99edfc };
.color3 { #088ccd };
.color4 { #559db5 };
.color5 { #acc4d1 };"""

custom_css = """
    <style>
        
        .h1-title { 
            text-align:center;
            margin:-55px;
            margin-bottom:70px;
            font-weight: bold;  
            font-size: 40px;
            color:white;
            
            
            
            
            
        }
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
        
        .container-main {
            position: relative;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            padding: 0px 0px;
            height: 400px; /* altura fixa */
            max-height: 400px; /* altura máxima */
            overflow-y: auto; /* habilita o scroll vertical */
            margin-top:150px;
            background-color: rgb(84, 176, 237, 0.7);
            border-radius: 20px;
            box-shadow: 0 0 0 rgba(0, 0, 0, 0.1);
            
            
    }
        .st-emotion-cache-z5fcl4 {
            width: 100%;
            padding: 6rem 1rem 10rem;
            min-width: auto;
            max-width: initial;
            overflow: hidden;
            background-color: #0000005c;
        }
   
        
        .container-main a {
            display: inline-block; /* Faz com que os itens da lista fiquem em linha */
            color:white;
            margin-left:60px;
            padding:10px;
            text-decoration: none;
            font-weight: bold;       /* Tornar o texto em negrito */
            font-size: 18px;   
            
            
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
custom_day = """
        @media (max-width:420px) {
            .day-weeke { 
                color:red;
                display:flex;
                flex-direction: row;
                justify-content: space-around;
    
        }
    }
"""