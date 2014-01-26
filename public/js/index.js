var choices = [];

// renders the new choices avalaible after 
// a new or revised decision is made
function onChoiceMade() {
	$(this).addClass('chosen');
	$(this).siblings().removeClass('chosen');

	// TODO: render handle childless choices

	var nextSteps = $(this).parent().nextAll().remove();
	choices.splice(choices.length - nextSteps.length);

	var thisIndex = $(this).prevAll().length;
	var thisChoice = choices[choices.length -1].children[thisIndex];
	choices.push(thisChoice);

	renderNextStep(thisChoice.children);
}

// returns an unattached row of all the next choices
function renderNextStep(children) {
	var step = $('<div class="step">');

	// TODO: render arrow pointing to target if no children

	children.forEach(function(choice){
		var $choice = $('<div class="choice">)');
		$choice.html(choice.industry +' '+ choice.title);
		$choice.click(onChoiceMade);
		step.append($choice);
	});

	$('#career-path').append(step);
}

// returns a promise for the json path
function requestPaths(destInd, destTitle, srcInd, srcTitle) {
	var fakeData = [{

		title: 'Accountant',
		industry: 'Dairy',
		description: 'I got experience crunching numbers',
		start: '10/20/11',
		end: '10/25/11',
		children: [{

			title: 'Producer',
			industry: 'Cinema',
			description: 'I made phone calls and made things happen',
			start: '10/10/97',
			end: '12/10/97' }, {

			title: 'Cashier',
			industry: 'Retail',
			description: 'I serviced customers',
			start: '8/11/12',
			end: '8/23/12',
			children: [{

				title: 'Producer',
				industry: 'Cinema',
				description: 'I made phone calls and made things happen',
				start: '2/10/97',
				end: '2/8/98' }]}]}, {

		title: 'Tester',
		industry: 'Video Games',
		description: 'I got my foot in the door of the bungie',
		start: '2/21/13',
		end: '1/5/03',
		children: [{

			title: 'Producer',
			industry: 'Cinema',
			description: 'I made phone calls and made things happen',
			start: '2/10/97',
			end: '2/8/98' }]
	}];

	return new $.Deferred().resolve(fakeData).promise();

	// // TODO: return this JSON request when server is ready
	// return $.getJSON('findPath', {
	// 	tjt: destTitle, 
	// 	tin: destInd,
	// 	cjt: srcTitle,
	// 	cin: srcInd
	// }).promise();
}

////////////////////////////////////////////////

// init chosen jquery plugin
var inputs = $('.industry, .title').chosen({
	inherit_select_classes: true,
	display_disabled_options: false
});

/////////////// event bindings /////////////////

$('#go-button').click(function(){
	// TODO: validate user input
	var params = {};

	requestPaths(params).then(function(children){
		choices = [{children:children}];
		renderNextStep(children);
	});
	// TODO: handle network errors
});

inputs.on('change', function(e, params) {
	var selection = params.selected;
	// TODO: update based on new selection
});