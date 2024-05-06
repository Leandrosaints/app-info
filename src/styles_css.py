
cores = """


    .color1 { #0444b4 };
    .color2 { #9ec4f1 };
    .color3 { #0444ac };
    .color4 { #033895 };
    .color5 { #b4c4dc };
        
"""
custom_css = """
    <style>
      
        .custom-container {
          
            height:400px;
            width:370px;
            margin: 0 auto;
            border-radius: 0.5rem;
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
            margin-top: 0px; /* Reduz a margem superior */
        }
        .custom-container h1 {
          
            text-align:center;
        }
     
        

    </style>
"""

custom_main = """
    <style>

        .container-main {
            position: absolute;
            top: 50%;
            left: 52%;
            transform: translate(-50%, -50%);
            padding:  0px 50px;
            width:360px;
            height:auto;
            margin-top:30px;
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            
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
        }
            
            
        
        
        #MainMenu {
            visibility: hidden;
            
        }
        footer {visibility: hidden;}
        
    </style> 
"""