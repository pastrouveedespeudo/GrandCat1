
<!DOCTYPE html>

<html>
    <head>
    
        <meta charset="utf-8" />
           
        <title>GrandPY</title>

   

        <link  rel="stylesheet" href="/static/styles/css/home.css" />

        
        <link rel="shortcut icon" href="/static/img/favicon.ico">
        
	<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
	<script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>

	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">


	<script async defer
    		src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCt2O8fe5cHDLkjjFk4TQ9Os5Y3vFGmqU8&callback=initMap">
	</script>

	
        <div class="container">
          <div class="row">
          
            <div class="col-lg-1 col-xs-12">
                <a href ="yo"><img src="static/images/image1.jpg" id="logo" alt="logo"/></a>
            </div>

    
            
            <div class="col-lg-10 col-xs-12">
              <h1>HOME</h1>
              <h2>Hey I'm GrandCat</h2>
              <h3>Site exclusivement réservé à la recherche d'adresse</h3>
          </div>
          
         </div>
      </div>




        </head>
            
        <body>
            


  <div class="essais" id ="essaie"></div>


  </form>
      
    <div class="container">
      <div class="row">
      
        <div id="image1" class="col-lg-2 col-xs-12">
          <img id="tourne" src="static/images/tourne/one.jpg"/>
          
        </div>
        
      
  
        <br>
        <div id="map" class="col-lg-6 col-xs-12">
          <img src="static/images/yo.jpg" id="payschat"/>
          <img src="static/images/p.jpg" id="payschat"/>
        </div>

      
    </div>
  

  
    <div class="container">
      <div class="row">

        <div id="monCadreWiki" class="class="col-lg-6 col-xs-12"></div>
    
        <div id="monCadre", class="class="col-lg-6 col-xs-12"></div>
        <br>
        <div class="class="col-lg-4 col-xs-12" id="inp">
          <form id="form_data">

            <input type="text" class="classRecupInfo" id="idRecupInfo" size="80" 
                placeholder="Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"/><br>

      
            <input type="submit" class="classButtonInput" id="idButtonInput" value="Enter"/>
            <center><img src="/static/images/chat_home.jpg" alt="imagecat" /></center>

         </form>
         

         
       </div>


</div>
</div>
      
      <div id="monCadreAlert"></div>  
    


      <div id = "heure" class ="heure"></div>

      


      <div class="divFavorite" id="divFavorite"></div>

      

   


    



        </body>















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
      


    $(document).ready(function(){
      $("#formPseudo").on("submit", function(ev){
     
        $.ajax({
          data:{
            data:$("#idRecupPseudo").val(),
          },
          type:"POST",
          url:"/login"


        })
        .done(function(data){

          if (data.error){
              $("#monCadreAlert").text(data.error);
              $("#divPseudo");
          }
          else{
              $("#divPseudo").html(data.data);
              $("#monCadreAlert");
              alert("fini")
              
              
          }


          });
          map();
          effacer();
          ev.preventDefault();
      
        });
      });

   
     function map(){

        
        document.getElementById("map").innerHTML = ""
        document.getElementById("map").style.width = "580px"
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
          //console.log(liste2)
          a = Number(liste2[liste2.length -3].slice(1,-1).join(''));
          b = Number(liste2[liste2.length -2].slice(2,-5).join(''));
          //console.log(liste2)
          //console.log(a)
          //console.log(b)
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

</html>














