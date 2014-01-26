var choices = [];

// renders the results in using d3
function render(graph) {
	var width = $('#career-path').width();
	var height = $('#career-path').height();

	var force = d3.layout.force()
		.charge(-350)
		.gravity(0)
		.friction(0.7)
		.linkDistance(80)
		.size([width,height])

	var svg = d3.select('#career-path').append('svg')
		.attr('width',width)
		.attr('height',height)

	force
		.nodes(graph.nodes)
		.links(graph.links)
		.start()

	var link = svg.selectAll(".link")
      .data(graph.links)
    .enter().append("line")
      .attr("class", "link")
      .style("stroke-width", "2px")
      //.style("stroke", "#222")

    var node = svg.selectAll(".node")
      .data(graph.nodes)
    .enter().append('g')
    	.attr('class','node')
    	.call(force.drag)

    node.append("circle")
      .attr("r", 30)
      .style("fill", "gray")

    node.append("text")
    	.attr('dy', '.3em')
    	.style('text-anchor', 'middle')
      .text(function(d) { console.log(d); return d.title; });

    force.on("tick", function() {
	    link.attr("x1", function(d) { return d.source.x; })
	        .attr("y1", function(d) { return d.source.y; })
	        .attr("x2", function(d) { return d.target.x; })
	        .attr("y2", function(d) { return d.target.y; });

	    node.attr('transform', function(d){ 
    		return "translate(" + d.x + "," + d.y + ")"; });

	    // node.attr("cx", function(d) { return d.x; })
	    //     .attr("cy", function(d) { return d.y; });
	});

}

// returns a promise for the json path
function requestPaths(destInd, destTitle, srcInd, srcTitle) {
	var fakeData = {
		nodes: [{

			title: 'Accountant',
			industry: 'Dairy',
			description: 'I got experience crunching numbers',
			start: '10/20/11',
			end: '10/25/11' }, {

			title: 'Producer',
			industry: 'Cinema',
			description: 'I made phone calls and made things happen',
			start: '10/10/97',
			end: '12/10/97' }, {

			title: 'Cashier',
			industry: 'Retail',
			description: 'I serviced customers',
			start: '8/11/12',
			end: '8/23/12' }, {

			title: 'Tester',
			industry: 'Video Games',
			description: 'I got my foot in the door of the bungie',
			start: '2/21/13',
			end: '1/5/03' }, {

			title: 'Designer',
			industry: 'Video Games',
			description: 'I drew concept art',
			start: '2/10/97',
			end: '2/8/98' }
		],

		links: [
			{source:2, target:0},
			{source:3, target:4},
			{source:2, target:4},
			{source:1, target:2},
			{source:4, target:2}
	]};

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

	requestPaths(params).then(render);
	// TODO: handle network errors
});

inputs.on('change', function(e, params) {
	var selection = params.selected;
	// TODO: update based on new selection
});