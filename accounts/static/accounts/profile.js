(function($){
	var csrfmiddlewaretoken = $("input[name=csrfmiddlewaretoken]").val();
	$("select[name=work_type]").on('change', function(){
		$.ajax({
			type: "POST",
			url: $("input[name=url2action]").val(),
			data: {
				csrfmiddlewaretoken: csrfmiddlewaretoken,
				worktype_pk: $("select[name=work_type]").val(),
			},
			success: function(data){
				//console.log(data)
				var expose = $('select[name=expose]');
				expose.html('');
				$.each(data, function(i, val){
					expose.append($("<option></option>")
						.attr("value",val.pk)
						//.prop("selected", city_current == value)
						.text(val.name)); 
				})
			}
		});
	});
	$('select[name=expose]').trigger('change');
})(jQuery);