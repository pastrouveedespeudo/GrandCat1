

<!DOCTYPE html>
<html lang="en">

<head>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">

  <title>Coming Soon - Start Bootstrap Theme</title>

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



                      #discussion{
                      border: 1px solid black;
                      width: 100%;
                      overflow:auto;
                      height:300px;
                      float:left;
                      background-color:# bd6242;
                      
                  }



                  #image{
                      position:relative;
                      border: 1px solid black;
                      width: 100%;
                      height:550px;
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

            
        </div>
    </div>


    
    <div class="container h-100">
      <div class="row h-100">
    

        <div class="col-12 my-auto">
        
          <div class="masthead-content text-white py-5 py-md-0">

            <h1 class="mb-3">I'm Grand Cat !</h1>


            <form id="form_raise">
             <div class="container col-xs-12 col-sm-12 col-md-12 col-lg-12">
                 <div class="row">

                      <div id="discussion" class="col-xs-offset-3 col-sm-offset-0 col-md-offset-0 col-lg-5">d</div>
                      <div class="col-xs-0 hidden-sm hidden-md col-lg-1"><br></div>
                      <div id="image" class="col-xs-offset-3 col-sm-offset-0 col-md-offset-0 col-lg-6"></div>
                      
                      <input type="submit" value="Effacer" id="effacer"
                            style="width:10%; border:2px solid black; height:50px; border-radius:10px; font-size: 1.2vw;
                            float:right;"/>

                     <input type="hidden" value="effacer" name="effacer" id="hiddeneffacer"/>
                </div>
            </div>

            </form>

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
                        font-size: 1.3vw;" id="idRecupInfo"><br>
          
                        <input type="submit" id="sub" value="Enter" id="idButtonInput"
                            style="width:15%; border:2px solid black; height:50px; border-radius:10px; font-size: 1.2vw;"/>
                       
 
                   </div>
                </div>
             </form>


            <p>Ai-je l'autorisation denregistrer la conversation ? oui, non</p>
                      
                 
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





MONCADRE = []

$(document).ready(function(){
  
  $("form").on("submit", function(e){
      
      $.ajax({
          data:{
              data:$("#idRecupInfo").val(),

          },
          type:"POST",
          url:"/reponse",


      })
      .done(function(data){

          if (data.error){
              $("#monCadreAlert").text(data.error);
              $("#image");
          }
          else{
              $("#image").html(data.data);
              $("#monCadreAlert");
            
              
          };


      });
      

      e.preventDefault();

      
  });
});






$(document).ready(function(){
  
  $("form").on("submit", function(e){
      
      $.ajax({
          data:{
              data:$("#idRecupInfo").val(),

          },
          type:"POST",
          url:"/img",

      })
      .done(function(data){

          if (data.error){
              $("#monCadreAlert").text(data.error);
              $("#discussion");
          }
          else{
              $("#discussion").html(data.data);
              $("#monCadreAlert");
            
              
          };


      });
      
      effacer();
      e.preventDefault();

      
  });
});






function effacer(){
  document.getElementById("idRecupInfo").value = "";
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


.masthead{position:relative;overflow:hidden;padding-bottom:15rem;z-index:2}

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






#inp{
  float:left;

}





<style>




















