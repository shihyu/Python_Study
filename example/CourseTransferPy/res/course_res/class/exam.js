CORRECT_ANSWER_STRING_COLOR = "#33CCCC";
CORRECT_ANSWER_STRING = " (正解)";
WRONG_ANSWER_STRING_COLOR = "#FF9999";

window.onload=function()
{
	return true;
};

window.onbeforeunload=function()
{
	this_score = document.F_SCORE.F_I_score.value;
	window.returnValue = this_score;
}

/** 
 * CallBack function
 */
 
$(document).ready(function() {
		$("#tSubmit").click(function()
		{
			thisscore = 0;
			totalscore = 0;
			for (var i=0; i<ans.length; i++)
			{
				thisscore = jq_GetScore(i);
				totalscore = thisscore + totalscore;
				if(gShowAnserVar)
					jq_ShowAnswer(i);
			}

			$("DIV#FORM_SUBMIT").css("display","none");
			$("DIV#MESSAGE1").css("display","none");

			$("#F_I_score").attr("value",totalscore);

			if(gShowScoreVar)
				jq_ShowScore(totalscore);

			if(gShowAnserVar)
			{
				$("select").css("font-size", "11pt");
				$("DIV#WIN_CLOSE").css("display","block");
			}

			return false;
 		});
		
		$("#tClose").click(function()
		{
			window.close();
 		});

		function jq_ShowScore(totalscore)
		{
				$("#RESULTS").css("display","block");
				$("DIV#MESSAGE2").css("display","block");
				$("#RESULTS").css("background-color","#FFFFFF");

				$("#RESULTS_SCORE").html(totalscore);
		}

		function jq_ShowAnswer(this_index)
		{
			answer_string = CORRECT_ANSWER_STRING_COLOR;

			var this_object_name = ans[this_index].name;
			var this_object_note = ans[this_index].note;
			var string1 = ans[this_index].answer;

			var this_item_type = ($("#FORM1 :input[name='"+this_object_name+"']").attr("type"));
			
			if(ans[this_index].noteref.length>0)
				this_object_note += "<IMG SRC='"+ans[this_index].noteref+"'>";
			if(string1.charAt(0) == '+')
			{
				string1 = string1.substr(1,(string1.length-1));
			}
			jQuery.each((string1.split(",")),function (i){
				switch(this_item_type)
				{
					case 'select-one':
					case 'select':
								$("#FORM1 :input[name='"+this_object_name+"']").css("background-color",WRONG_ANSWER_STRING_COLOR)
								if($("#FORM1 :input[name='"+this_object_name+"']").val() == this)
									answer_string = CORRECT_ANSWER_STRING_COLOR;

								($("#FORM1 :input[name='"+this_object_name+"'] option[value='"+this+"']").append(CORRECT_ANSWER_STRING));
							break;
					case 'radio':
								if(($("#FORM1 :input[name='"+this_object_name+"']:checked").val()) != this)
									answer_string = WRONG_ANSWER_STRING_COLOR;

								($("#FORM1 :input[name='"+this_object_name+"'][value='"+this+"']").after(CORRECT_ANSWER_STRING));

							break;
					case 'checkbox':
								if(!($("#FORM1 :input[name='"+this_object_name+"'][value='"+this+"']").attr("checked")))
									answer_string = WRONG_ANSWER_STRING_COLOR;

								($("#FORM1 :input[name='"+this_object_name+"'][value='"+this+"']").after(CORRECT_ANSWER_STRING));
							break;
					default:
							break;
				}
					$("#FORM1 :input[name='"+this_object_name+"'][value='"+this+"']").css("background-color",answer_string);
			});
			$("DIV#"+this_object_name+"").css("display","block");
			$("DIV#"+this_object_name+"").append(this_object_note);
		}

		function jq_GetScore(this_index)
		{
			this_object_name = ans[this_index].name;
			this_object_answer = ans[this_index].answer;
			this_object_score = ans[this_index].score;

			this_item_type = ($("#FORM1 :input[name='"+this_object_name+"']").attr("type"));
			this_item = ($("#FORM1 :input[name='"+this_object_name+"']"));

			switch(this_item_type)
			{
				case 'select-one':
				case 'select':
						this_item_value = ($("#FORM1 :input[name='"+this_object_name+"']").val());
						if(this_item_value != this_object_answer)
							this_object_score = 0;
						break;
				case 'radio':
						this_item_value = ($("#FORM1 :input[name='"+this_object_name+"']:checked").val());
						if(this_item_value != this_object_answer)
							this_object_score = 0;
						break;
				case 'checkbox':
						this_item_value = "";
						$("#FORM1 :input[name='"+this_object_name+"']:checked").each(function(i){
							(this_item_value.length ==0)?	(this_item_value =  $(this).val()):(	this_item_value = this_item_value + "," + $(this).val() );
						});
						this_compare_result = jq_CompareString(this_item_value,this_object_answer);
						if(this_compare_result > 0)
							this_object_score = this_object_score * this_compare_result;
						else
							this_object_score = 0;
						break;
				default:
							this_object_score = 0;
						break;
			}
			return this_object_score;
		}

		function jq_CompareString(string1,string2)
		{
			var c_ary1 = ((string1.split(",")).sort()).join(",");
			var c_ary2 = ((string2.split(",")).sort()).join(",");

			var correct_count = 0;
			var answer_length = (string2.split(",")).length;
			if(string2.charAt(0) == '+')
			{
				string2 = string2.substr(1,(string2.length-1));
				jQuery.each((string1.split(",")),function(i)	{
						if((string2.indexOf(this)) >= 0)
							correct_count++;
					}
				 );
			}
			else
			{
				if(c_ary1==c_ary2)
					correct_count = answer_length;
			}
		 return (correct_count/answer_length);
		}
});