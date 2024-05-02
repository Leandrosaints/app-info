

custom_css = """
    <style>

        .custom-container {
          
            height:400px;
            width:370px;
            margin:0, 0, 20px, 0;
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
            padding: 50px;
            width:360px;
            height:300px;
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
        .container-main h5 {
            font-size:18px;
            margin-left:2px;   
    }


    </style>
"""

custom_menu = {

    "container": {
        "height": "100px",
        "padding": "0!important",
        "background-color": "#fafafa"
    },

    "icon": {"color": "orange", "font-size": "25px"},
    "nav-link": {
        "font-size": "16px",
        "text-align": "center",
        "margin": "0px",
        "--hover-color": "#eee"
    },
    "nav-link-selected": {"background-color": "green"}
}
# Aplicar os estilos CSS personalizados
