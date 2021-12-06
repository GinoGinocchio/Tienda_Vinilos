var updateBtns= document.getElementsByClassName('update-cart')

for(i = 0; i < updateBtns.length;i++ ){
    updateBtns[i].addEventListener('click',function(){
        var productId= this.dataset.product   
        var action = this.dataset.action
        console.log('productId:', productId, 'Action:', action )

        console.log('USER:', user)
        if (user=='AnonymousUser'){
            Swal.fire({
                title: "Ingrese con su cuenta",
                icon: "warning" 
              })
           //console.log("usuario no registrado") 

        } else {          
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId, action){
    console.log('Usuario conectado, enviando informacion')

    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,

        },
        body: JSON.stringify({'productId': productId,'action': action })
    })

    .then((response) => {
        return response.json()
    })

    .then((data) => {
        location.reload()
    });
}

const showsdata_synchronized=()=>{
          
setInterval(() => {
    fetch(' https://mourits-lyrics.p.rapidapi.com/cacheCount')
        .then(response => response.json())
        .then(data_json => {
         // console.log(data_json)
         const Vinilos=[]   
         //data_json.forEach(e=>{
           //negocio.push(e.numeroPuerta)
         //})
         for(let i=0;i<5;i++){
           Vinilos.push(data_json[i].sing)
           Vinilos[i]="Data vinillo"+" "+sing[i]
         }
          
        // console.log(numeroPuerta,codigoSeguimiento)
         chart.updateSeries([{
           data: Vinilos
         }])
         chart.updateOptions({
           xaxis:{
            categories:Vinilos
           }
         })

       // data_json.forEach(e => {
 
          //    cantidad.push(e.cantidad)             
         // }); 
           
        })
  }, 1000);
}