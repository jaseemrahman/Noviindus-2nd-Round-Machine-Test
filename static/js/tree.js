function last_child(element) {
    // var form = $('#form');
    console.log("last child")

    var book;
    book = document.getElementById("book").value;
    console.log(book)
    var direction = document.getElementById('direction').value;
    console.log(direction)
    // var formdata = form.serializeArray();
    // alert(formdata);
    // console.log(formdata)
	$.ajax({
        
        url:'/ajax',
        type: 'get',
        dataType: 'json',
        data:{
            book:book,
            direction:direction,},
            // csrfmiddlewaretoken:csrftoken},
        // beforeSend: function () {
        //   $("#modal-book").modal("show");
        // },
        success: function (data) {
			// $("#bs4-table tbody").html(data.html_book_list_category);  
            alert(data['last_child']);
            // document.getElementById("demo").innerHTML = data['last_child']
        }
      });
  };


