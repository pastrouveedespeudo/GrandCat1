
<!DOCTYPE html>
<html lang="en">

<head>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">

  <title>Coming Soon - Start Bootstrap Theme</title>


        <script async defer
                src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCt2O8fe5cHDLkjjFk4TQ9Os5Y3vFGmqU8&callback=initMap">
        </script>

  <!-- Bootstrap core CSS -->
  <link href="static/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

  <!-- Custom fonts for this template -->
  <link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:200,200i,300,300i,400,400i,600,600i,700,700i,900,900i" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css?family=Merriweather:300,300i,400,400i,700,700i,900,900i" rel="stylesheet">
  <link href="static/vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">

  <!-- Custom styles for this template -->


</head>

<body>
    



  <div class="masthead">

  
  <!-- logo -->
  <style>
  

  #logoo{
          margin-top:10px;
          border-radius:10px;
          width:15%;
          margin-left:10px;
          display: flex;
          min-width:30px;
          min-height:30px;
          border:3px solid black;
        }
    
 #tourne{
  margin-top:10px;
   border-radius:10px;
   width:30%;
   float:right;

   
   display: flex;
          

   min-width:50px;
   min-height:50px;
   max-width:120px;
   border:3px solid black;
   
   max-height:200px;
 }
 
 #map{
    width:100%;
    text-align:center;
     }

     
    #payschat{
    width:25%;
    height:70%;

 }



                      #monCadreWiki{
                      border: 1px solid black;
                      width: 100%;
                      overflow:auto;
                      height:150px;
                      float:left;
                      background-color:# bd6242;
                      
                  }



                  #monCadre{
                      position:relative;
                      border: 1px solid black;
                      width: 100%;
                      height:150px;
                      overflow:auto;
                      float:left;
                      background-color:# bd6242;
                  }

  </style>
  


  
    <div class="masthead-bg"></div>

    <div class="container col-xs-12 col-sm-12 col-md-12 col-lg-12">
        <div class="row">
        
            <div class="col-xs-5 col-sm-5 col-md-5 col-lg-5">
                <img src="static/images/image1.jpg" id="logoo" alt="logo"/>
            </div>
            
            <div class="col-xs-5 col-sm-5 col-md-5 col-lg-6" style="height:100px;">
                <img id="tourne" src="static/images/tourne/one.jpg"/>
            </div>
            
        </div>
    </div>


    
    <div class="container h-100">
      <div class="row h-100">
    

        <div class="col-12 my-auto">
        
          <div class="masthead-content text-white py-5 py-md-0">

            <h1 class="mb-3">I'm Grand Cat !</h1>
            <h5 class="mb-5" id="p">Entrez une addresse ! on la cherche pour vous, allez donc essayer note tchat !</h5>



              <div class="container col-xs-12 col-sm-12 col-md-12 col-lg-12">
                  <div class="row">
               
                      <div id="map" class="col-xs-12 col-sm-12 col-md-12 col-lg-12">
                        <img src="static/images/yo.jpg" id="payschat"/>
                        <img src="static/images/p.jpg" id="payschat"/>
                      </div>
               
                  </div>
              </div>

            <br>

             <div class="container col-xs-12 col-sm-12 col-md-12 col-lg-12">
                 <div class="row">

                      <div id="monCadre" class="col-xs-offset-3 col-sm-offset-0 col-md-offset-0 col-lg-5"></div>
                      <div class="col-xs-0 hidden-sm hidden-md col-lg-1"><br></div>
                      <div id="monCadreWiki" class="col-xs-offset-3 col-sm-offset-0 col-md-offset-0 col-lg-6"></div>           
                </div>
            </div>



            <style>
            #sub{
                margin-left:auto;
            }
            </style>



            <br>
            <form id="form_data">
                <div class="container col-xs-12 col-sm-12 col-md-12 col-lg-12 style="text-align:center;" id="ud">
                    <div class="row">
                    
                        
                        <input type="text" style="width:84%; text-align:center; border-radius:10px; border:2px solid black; height:50px;
                        font-size: 1.3vw;" id="idRecupInfo"
                            placeholder="Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"/><br>
          
                        <input type="submit" id="sub" value="Enter" id="idButtonInput"
                            style="width:15%; border:2px solid black; height:50px; border-radius:10px; font-size: 1.2vw;"/>
                       
 
                   </div>
                </div>
             </form>



                      
                 
        </div>
    </div>

            <div id="monCadreAlert"></div>  
          


            <div id = "heure" class ="heure"></div>

            


            <div class="divFavorite" id="divFavorite"></div>
          
              



  <!-- Bootstrap core JavaScript -->
  <script src="static/vendor/jquery/jquery.min.js"></script>
  <script src="static/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

  <!-- Custom scripts for this template -->


</body>

</html>





<script>
        var liste_image_logo = ["/static/images/loading/one.jpg",
                              "/static/images/loading/two.jpg",
                              "/static/images/loading/one.jpg",
                              "/static/images/loading/two.jpg",
                              "/static/images/loading/one.jpg",
                              "/static/images/loading/two.jpg",
                              "/static/images/loading/three.jpg"];


        var liste_image_logo_i = 0

        function change_image(){
        document.getElementById('tourne').src = liste_image_logo[liste_image_logo_i];
        if(liste_image_logo_i < liste_image_logo.length - 1){
          liste_image_logo_i++
        }
        else{
          liste_image_logo_i = 0
        }
        };



        var time;
        function start_logo_loading(){
        time = window.setInterval("change_image()", 1000);
        }


        function stop_logo_loading(){
        clearTimeout(time);
        }









        function map(){


          document.getElementById("map").innerHTML = ""
          document.getElementById("map").style.width = "100%"
          document.getElementById("map").style.height = "200px"


        }




        MONCADRE = []

        $(document).ready(function(){
          
          $("form").on("submit", function(e){
              start_logo_loading();
              $.ajax({
                  data:{
                      data:$("#idRecupInfo").val(),

                  },
                  type:"POST",
                  url:"/data"

                  

              })
              .done(function(data){

                  if (data.error){
                      $("#monCadreAlert").text(data.error);
                      $("#monCadre");
                  }
                  else{
                      $("#monCadre").html(data.data);
                      $("#monCadreAlert");
                      initMap();
                      
                  };


              });
              
              
              add_favorite();
              e.preventDefault();
              map();
              
          });
        });




        MONCADRE_WKI = []

        $(document).ready(function(){
          var finish2 = []
          $("form").on("submit", function(ev){

              $.ajax({
                  data:{
                      data:$("#idRecupInfo").val(),

                  },
                  type:"POST",
                  url:"/wiki"
                  

              })
              
              .done(function(data){

                  if (data.error){
                      $("#monCadreAlert").text(data.error);
                      $("#monCadreWiki");
                  }
                  else{
                      $("#monCadreWiki").html(data.data);
                      $("#monCadreAlert");
                      stop_logo_loading();
                      
                  }
              });
              
              effacer();
              ev.preventDefault();
          
          });
        });





        function add_favorite(){
        var ask = '  <center>Voulez vous ajouter cette adresse à vos favoris ?</center> \
                    <form> \
                    <input type="submit" class="classButtonInput" id="idButtonInput" value="Oui"/> \
                    <input type="submit" class="classButtonInput" id="idButtonInput" value="Non"/> \
                    <form>'


        document.getElementById("divFavorite").innerHTML = ask
        //ici faire un post
        //et document.getElementById("divFavorite").innerHTML = ""

        };




        function initMap(){
          
          liste = [[],[],[],[],[],[],[],[],
                   [],[],[],[],[],[],[],[],
                   [],[],[],[],[],[],[],[],
                   [],[],[],[],[],[],[],[],
                   [],[],[],[],[],[],[],[],
                   [],[],[],[],[],[],[],[],
                   [],[],[],[],[],[],[],[],
                   [],[],[],[],[],[],[],[],
                   [],[],[],[],[],[],[],[],
                   [],[],[],[],[],[],[],[],
                   [],[],[],[],[],[],[],[],
                   [],[],[],[],[],[],[],[],
                   [],[],[],[],[],[],[],[],
                   [],[],[],[],[],[],[],[],
                   [],[],[],[],[],[],[],[],
                   [],[],[],[],[],[],[],[],
                   [],[],[],[],[],[],[],[],
                   [],[],[],[],[],[],[],[],
                   [],[],[],[],[],[],[],[],
                   [],[],[],[],[],[],[],[],
                   [],[],[],[],[],[],[],[],
                   [],[],[],[],[],[],[],[],
                   [],[],[],[],[],[],[],[],
                   [],[],[],[],[],[],[],[],
                   [],[],[],[],[],[],[],[],
                   [],[],[],[],[],[],[],[],
                   [],[],[],[],[],[],[],[],
                   [],[],[],[],[],[],[],[],
                   [],[],[],[],[],[],[],[],
                   [],[],[],[],[],[],[],[],
                   [],[],[],[],[],[],[],[],
                   [],[],[],[],[],[],[],[],
                   [],[],[],[],[],[],[],[],
                   [],[],[],[],[],[],[],[],
                   [],[],[],[],[],[],[],[],
                   [],[],[],[],[],[],[],[]]
          
          liste2 = []
          
          var c = document.getElementById("monCadre");
      
          var a = c.innerText || c.textContent;
          var b = a.length;
          //console.log(a)
          
          var c = 0;

          for(var i = 0; i<=b;i++){
            liste[c].push(a[i]);
            if(a[i] === ","){
                c++;
                };
          };

          for(var i =0;i<=liste.length;i++){
              if(liste[i]!=""){
                  liste2.push(liste[i]);
              }
           };
          console.log(liste2)
          a = Number(liste2[liste2.length -3].slice(1,-1).join(''));
          //b = Number(liste2[liste2.length -2].slice(2,-5).join(''));
          b = Number(liste2[liste2.length -2].slice(1,-4).join(''));
          //console.log(liste2)
          console.log(a)
          console.log(b)
          //console.log(liste2.length -2)


          var options = {
              zoom:13,
              center:{lat:a,lng:b}
          }
          var map = new google.maps.Map(document.getElementById("map"), options);
        } 





        function effacer(){
          document.getElementById("idRecupInfo").value = "";
        }



        function imageTourne(){
          document.getElementById('nom-de-ta-photo').src= "l'url de ta nouvelle image";
        }




</script>

























<style>



html{height:100%}

body{
    height:100%;
    position:relative;
    font-family:'Source Sans Pro';
     background-color:#cd9557;
    }


h1{
    font-family:Merriweather;
    font-weight:700;
    font-size: 1.75vw;
    }


h2,h3,h4,h5,h6{
    font-family:Merriweather;
    font-weight:700;
    font-size: 1.6vw;
    }


.masthead{position:relative;overflow:hidden;padding-bottom:5rem;z-index:2}

.masthead .masthead-bg{
	


#map{
  width:100%;
  margin-top:auto;

}
#payschat{
  width:20%;
  height:80%;


}


#monCadreWiki{
    border: 2px solid black;
    width: 100%;
    overflow:scroll;
    height:150px;
    float:left;
}




#monCadre{
    position:relative;
    border:2px solid black;
    width: 100%;
    height:150px;
    overflow:scroll;
    float:left;
}

#supp{

  width:30%;
  max-width:100px;
}



form{
    text-align:center;
}

p{
    text-align:center;
}

#blockinput{
    text-align:center;
}

.classRecupInfo{
    text-align:center;
    font-style:italic;
    margin:0 auto;
}


#image1{
  float:right;
}


#c{
 float:left;
 color:red;
}
.formPseudo{
    margin-top:-200;
    margin-right:910px;
}


#divFavorite{
  margin-right:0 auto;
}



#inp{
  float:left;

}



}


<style>





















