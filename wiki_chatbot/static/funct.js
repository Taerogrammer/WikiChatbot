function funct() {

    var q = document.getElementById("question").value;

    console.log(q);
    var data = {"question" : q}

    $.ajax({
        type: "POST",
        url: "/answer_2",
        dataType: 'text',
        contentType : 'application/JSON; charset=utf-8',
        processData: false,
        data: JSON.stringify(data),
        cache: false,
        success: function (response) {
          console.log(response);
	  var words = response.split('**', 4);
	  console.log(words);
	  console.log("=================");
	  console.log(words[0]);
	  console.log(typeof(words[1]));
	  console.log("=-------------------");
//	  console.log(words[1]);
		
	  console.log("--------------------------");
	
	// x1= words[1].indexOf('<<<<<');
	// x2= words[1].indexOf('>>>>>');

	
	 
	find_start = " <<<<< ";
	find_end = " >>>>> ";
	
	words[2] = words[2].split(" <<<<< ").join("<span class='highlight'> ");
	words[2] = words[2].split(" >>>>> ").join("</span>");
	

	console.log(words[1])


//	words[1].replace(regex, "<span class='highlight'>" + find_start + "</span>");
//	words[1].replace(regex, "<span class='highlight'>" + find_end + "</span>");  
	

          document.getElementById('answer_generate').innerText=words[0];
	  document.getElementById('tensor').innerText=words[1];
	  document.getElementById('wiki_context').innerHTML=words[2];
	  document.getElementById('wiki_url').setAttribute("href", words[3]);
        }
    })  

}
