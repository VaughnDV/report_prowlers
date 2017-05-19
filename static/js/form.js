//Slick in the static file 


  $(document).ready(function(){
    $('.Slider').slick({
        slidesToShow: 4,
      slidesToScroll: 1,
      autoplay: true,
      autoplaySpeed: 1000,
    });
  });




// getting the item info

  $(function() {

    var itemObject = new Object();

    $('#MS').on('click', function() {
      itemObject.material = this.id
      $('#SS304').toggle(300);
      $('#SS316').toggle(300);
      $('#sizeMS').toggle(300);
      $('#SSchedule').hide(300);
      $('#MSchedule').hide(300);
      $('#Flanges').hide(300);
      $('#Shape').hide(300);
    });

    $('#SS304').on('click', function() {
      itemObject.material = this.id
      $('#MS').toggle(300);
      $('#SS316').toggle(300);
      $('#sizeSS').toggle(300);
      $('#SSchedule').hide(300);
      $('#MSchedule').hide(300);
      $('#Flanges').hide(300);
      $('#Shape').hide(300)
    });

    $('#SS316').on('click', function() {
      itemObject.material = this.id
      $('#SS304').toggle(300);
      $('#MS').toggle(300);
      $('#sizeSS').toggle(300);
      $('#SSchedule').hide(300);
      $('#MSchedule').hide(300);
      $('#Flanges').hide(300);
      $('#Shape').hide(300)
    });
        
        // MS Sizes
    $('#MS50NB').on('click', function() {
      itemObject.size = this.id
      $('#MS65NB').toggle(300);
      $('#MS80NB').toggle(300);
      $('#MSchedule').toggle(300);
    });

    $('#MS65NB').on('click', function() {
      itemObject.size = this.id
      $('#MS50NB').toggle(300);
      $('#MS80NB').toggle(300);
      $('#MSchedule').toggle(300);
    });

    $('#MS80NB').on('click', function() {
      itemObject.size = this.id
      $('#MS65NB').toggle(300);
      $('#MS50NB').toggle(300);
      $('#MSchedule').toggle(300);
    });

    // SS Sizes 

    $('#SS50NB').on('click', function() {
      itemObject.size = this.id
      $('#SS65NB').toggle(300);
      $('#SS80NB').toggle(300);
      $('#SSchedule').toggle(300);
    });

    $('#SS65NB').on('click', function() {
      itemObject.size = this.id
      $('#SS50NB').toggle(300);
      $('#SS80NB').toggle(300);
      $('#SSchedule').toggle(300);
    });

    $('#SS80NB').on('click', function() {
      itemObject.size = this.id
      $('#SS65NB').toggle(300);
      $('#SS50NB').toggle(300);
      $('#SSchedule').toggle(300);
    });

    // Stainless Pipe Schedule  

    $('#Shed5').on('click', function() {
      itemObject.pipe = this.id
      $('#Shed10').hide(300);
      $('#Shed40').hide(300);
      $('#Flanges').show(300);
    });

    $('#Shed10').on('click', function() {
      itemObject.pipe = this.id
      $('#Shed5').hide(300);
      $('#Shed40').hide(300);
      $('#Flanges').show(300);
    });

    $('#Shed40').on('click', function() {
      itemObject.pipe = this.id
      $('#Shed10').hide(300);
      $('#Shed5').hide(300);
      $('#Flanges').show(300);
    });

    // Mildsteel Pipe Schedule 

    $('#Light').on('click', function() {
      itemObject.pipe = this.id
      $('#Medium').hide(300);
      $('#Heavy').hide(300);
      $('#Flanges').show(300);
    });

    $('#Medium').on('click', function() {
      itemObject.pipe = this.id
      $('#Light').hide(300);
      $('#Heavy').hide(300);
      $('#Flanges').show(300);
    });

    $('#Heavy').on('click', function() {
      itemObject.pipe = this.id
      $('#Light').hide(300);
      $('#Medium').hide(300);
      $('#Flanges').show(300);
    });

    // Flanges

    $('#F1000-3').on('click', function() {
      itemObject.flanges = this.id
      $('#F1600-3').hide(300);
      $('#F2500-3').hide(300);
      $('#Shape').show(300);
    });


    $('#F1600-3').on('click', function() {
      itemObject.flanges = this.id
      $('#F1000-3').hide(300);
      $('#F2500-3').hide(300);
      $('#Shape').show(300);
    });


    $('#F2500-3').on('click', function() {
      itemObject.flanges = this.id
      $('#F1600-3').hide(300);
      $('#F1000-3').hide(300);
      $('#Shape').show(300);
    });

    // Shape
    $('#StrPipe').on('click', function() {
      itemObject.shape = this.id
      $('#Elbow').hide(300);
      $('#Tee').hide(300);
      $('#Manifold').hide(300);
      $('#Reducer').hide(300);
      $('#Blank').hide(300);
      $('#Other').hide(300);
      $('#PlainOrFlanged').show(300);
    });    

    $('#Elbow').on('click', function() {
      itemObject.shape = this.id
      $('#StrPipe').hide(300);
      $('#Tee').hide(300);
      $('#Manifold').hide(300);
      $('#Reducer').hide(300);
      $('#Blank').hide(300);
      $('#Other').hide(300);
      $('#PlainOrFlanged').show(300);
    }); 

    $('#Tee').on('click', function() {
      itemObject.shape = this.id
      $('#Elbow').hide(300);
      $('#StrPipe').hide(300);
      $('#Manifold').hide(300);
      $('#Reducer').hide(300);
      $('#Blank').hide(300);
      $('#Other').hide(300);
      $('#PlainOrFlangedPlus').show(300);
    });     

    $('#Manifold').on('click', function() {
      itemObject.shape = this.id
      $('#Elbow').hide(300);
      $('#Tee').hide(300);
      $('#StrPipe').hide(300);
      $('#Reducer').hide(300);
      $('#Blank').hide(300);
      $('#Other').hide(300);
      $('#PlainOrFlangedPlus').show(300);
    }); 

    $('#Reducer').on('click', function() {
      itemObject.shape = this.id
      $('#Elbow').hide(300);
      $('#Tee').hide(300);
      $('#Manifold').hide(300);
      $('#StrPipe').hide(300);
      $('#Blank').hide(300);
      $('#Other').hide(300);
      $('#ReducedSize').show(300);
    }); 

    $('#Blank').on('click', function() {
      itemObject.shape = this.id
      $('#Elbow').hide(300);
      $('#Tee').hide(300);
      $('#Manifold').hide(300);
      $('#Reducer').hide(300);
      $('#StrPipe').hide(300);
      $('#Other').hide(300);
      $('#Coating').show(300);
    }); 

    $('#Other').on('click', function() {

      $('#Shape').hide(300);
      $('#ExtraShape').show(300);
    });

    $('#FBE').on('click', function() {
      itemObject.ends = this.id
      $('#FOE').hide(300);
      $('#PBE').hide(300);
      $('#Coating').show(300);
    });

    $('#F0E').on('click', function() {
      itemObject.ends = this.id
      $('#FBE').hide(300);
      $('#PBE').hide(300);
      $('#Coating').show(300);
    });

    $('#PBE').on('click', function() {
      itemObject.ends = this.id
      $('#FOE').hide(300);
      $('#FBE').hide(300);
      $('#Coating').show(300);
    });

    $('#FAE').on('click', function() {
      itemObject.ends = this.id
      $('#FBranches').hide(300);
      $('#FInline').hide(300);
      $('#BranchReduce').show(300);
    });

    $('#FBranches').on('click', function() {
      itemObject.ends = this.id
      $('#FAE').hide(300);
      $('#FInline').hide(300);
      $('#BranchReduce').show(300);
    });

    $('#FInline').on('click', function() {
      itemObject.ends = this.id
      $('#FAE').hide(300);
      $('#FBranches').hide(300);
      $('#BranchReduce').show(300);
    });

    $('#Galv').on('click', function() {
      itemObject.coating = this.id
      $('#FBEpoxy').hide(300);
      $('#FBEandEpoxy').hide(300);
      $('#None').hide(300);
      $('#Submit').show(300);
    });

    $('#FBEpoxy').on('click', function() {
      itemObject.coating = this.id
      $('#Galv').hide(300);
      $('#FBEandEpoxy').hide(300);
      $('#None').hide(300);
      $('#Submit').show(300);
    });

    $('#FBEandEpoxy').on('click', function() {
      itemObject.coating = this.id
      $('#FBEpoxy').hide(300);
      $('#Galv').hide(300);
      $('#None').hide(300);
      $('#Submit').show(300);
    });


    // Branches Reduce Or Not

    $('#SameSize').on('click', function() {
      itemObject.redBranch = this.id
      $('#ReducedSize').hide(300);
      $('#Coating').show(300);
    });    

    $('#ReduceSize').on('click', function() {
      itemObject.redBranch = this.id
      $('#SameSize').hide(300);
      $('#ReducedSize').show(300);
    });    

        // Reduced Sizes 

    $('#R50NB').on('click', function() {
      itemObject.redSize = this.id
      $('#R65NB').hide(300);
      $('#R80NB').hide(300);
      $('#ReducedFlange').show(300);
    });

    $('#R65NB').on('click', function() {
      itemObject.redSize = this.id
      $('#R50NB').hide(300);
      $('#R80NB').hide(300);
      $('#ReducedFlange').show(300);
    });

    $('#R80NB').on('click', function() {
      itemObject.redSize = this.id
      $('#R65NB').hide(300);
      $('#R50NB').hide(300);
      $('#ReducedFlange').show(300);
    });

    // Reduced Flange Type

    $('#R1000-3').on('click', function() {
      itemObject.redFlange = this.id
      $('#R1600-3').hide(300);
      $('#R2500-3').hide(300);
      $('#Coating').show(300);
    });


    $('#R1600-3').on('click', function() {
      itemObject.redFlange = this.id
      $('#R1000-3').hide(300);
      $('#R2500-3').hide(300);
      $('#Coating').show(300);
    });


    $('#R2500-3').on('click', function() {
      itemObject.redFlange = this.id
      $('#R1600-3').hide(300);
      $('#R1000-3').hide(300);
      $('#Coating').show(300);
    });


    // Reset Button
    $('#Reset').click(function() {location.reload();});





    // Submit Button
    $('#Submit').click(function() {

       //$("button:visible").each(function(){
          // $(element).is(":visible");
          //var key = $(this.name).val();
          //var value = $(this.name).val(); 
          //var feature = { key : value };
          //list.push(feature);
          //console.log(this.id);
        //});

       var jsonObject = JSON.stringify(itemObject);
       console.log(jsonObject);

      $.ajax({
        data : {jsonObject : jsonObject},
        type : 'POST',
        url : '/process',
        error: function(e){
          console.log(e);
           },
        //dataType: "json",
        //contentType: "application/json; charset=utf-8",
        //context: this,
      }).done(function(data) {

        if (data.error) {
          console.log(data.error)
          
        }
        else {
         console.log(data.name)
        }

      });

    //event.preventDefault();

  });





    // Info Button
    $('#Info').click(function() {
      
      $( "div:visible" ).click(function() {
        $( this ).css( "background", "yellow" );
      });
    });
  });

