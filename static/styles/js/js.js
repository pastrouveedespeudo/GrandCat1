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
    };
};


var time;
function start_logo_loading(){
    time = window.setInterval("change_image()", 1000);
};


function stop_logo_loading(){
    clearTimeout(time);
};


function map(){
  document.getElementById("map").innerHTML = "";
  document.getElementById("map").style.width = "100%";
  document.getElementById("map").style.height = "200px";
};


MONCADRE = []

$(document).ready(function(){
  $("form").on("submit", function(e){
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
  start_logo_loading();
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

    document.getElementById("divFavorite").innerHTML = ask;
};



function initMap(){
  liste = []
  var c = document.getElementById("monCadreHidden");
  var d = document.getElementById("monCadreHidden2");
  var monTexte = c.innerText || c.textContent;
  var monTexte2 = d.innerText || d.textContent;
  var a = Number(monTexte);
  var b = Number(monTexte2);
  var options = {
      zoom:13,
      center:{lat:a,lng:b}
  }
  var map = new google.maps.Map(document.getElementById("map"), options);
  stop_logo_loading();
}; 



function effacer(){
  document.getElementById("idRecupInfo").value = "";
};


function imageTourne(){
  document.getElementById('nom-de-ta-photo').src= "l'url de ta nouvelle image";
};


