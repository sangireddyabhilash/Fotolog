(function() {
   
   function populateDenominationList(vals) {
     document.getElementById('2g')
     var denoms = document.getElementById("denominations");
     denoms.selectedIndex = -1
     denoms.options.length = 0
     for (var i = 0; i < vals.length; i++) {
       var option = document.createElement("option");
       option.text = vals[i];
       denoms.appendChild(option);
     }
   }
   
   var plan2g = document.getElementById('2g')
   var plan3g = document.getElementById('3g')
   var planftt = document.getElementById('ftt')
   
   plan2g.addEventListener('click', 
       function() {
           console.log('2g plan selected')
           get2GDenominations(populateDenominationList)
       });
   
   plan3g.addEventListener('click', 
       function() {
           console.log('3g plan selected')
           get3GDenominations(populateDenominationList)
       });
   
   planftt.addEventListener('click', 
       function() {
           console.log('ftt plan selected')
           getFullTalktimeDenominations(populateDenominationList)
       });
   
   get2GDenominations(populateDenominationList)
})()
