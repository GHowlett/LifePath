/* General styling. */

body {
	background-color: #FFFFFF;
}
body, div, input, select {
	font-family: Tahoma, Geneva, sans-serif;
	font-size: 8pt;
	color: #333333;
}
a:link, a:visited, a:active {
	color: #000000;
	text-decoration: none;
}
a:hover {
	color: #80BC00;
}
form, fieldset, p, ul, ol {
	border: 0;
	margin: 0;
	padding: 0;
}
dt, legend, #footer {
	display: none;
}
img {
	border: 0;
	margin: 1px;
	padding: 0;
	vertical-align: middle;
}
abbr {
	border: 0;
}
.highlight {
	background-color: #FCFCA0;
}

/* Toggle display settings */

.default #preview, .default #smileys, .default #navigation, .extra #messages, .extra #paging {
	display: none;
}
.extra #preview, .extra #smileys, .extra #navigation, .default #messages, .default #paging {
	display: block;
}
.idle {
	opacity: 0.5;
	-moz-opacity: 0.5;
	-khtml-opacity: 0.5;
	filter: alpha(opacity=50);
}

/* Layout positioning. */

body {
	text-align: center;
	border: 0;
	width: 100%;
	height: 100%;
	margin: 0;
	padding: 0;
	overflow: hidden;
}
* html body {
	padding: 1.8em 0 9.6em 0;
}
#shoutbox {
	width: 100%;
	height: 100%;
}
#info {
	text-align: left;
	position: absolute;
	top: 0;
	right: 0;
	left: 0;
	padding: 3px 5px;
}
#control {
	position: absolute;
	right: 0;
	bottom: 0;
	left: 0;
	height: 9.2em;
	margin: 0;
	padding: 0;
}
#contents {
	position: absolute;
	top: 1.8em;
	right: 3px;
	bottom: 9.6em;
	left: 3px;
	margin: 0;
	padding: 0;
	overflow: auto;
}
* html #contents {
	width: 96%;
	height: 100%;
	margin: 0 auto;
}

/* Info bar. */

#info li {
	display: inline;
}
#info .icon a:link, #info .icon a:visited, #info .icon a:active {
	color: #80BC00;
}
#info li.icon {
	float: right;
}
#info li.text {
	display: block;
	height: 1.2em;
	overflow: hidden;
}

/* Form control. */

#control h2 {
	font-size: 7pt;
	font-weight: normal;
	line-height: 7pt;
	color: #999999;
	background-color: #F6F6F6;
	margin: 0 3px 2px 3px;
	padding: 2px;
}
#control h2 a {
	text-decoration: underline;
}
#control ul {
	line-height: 8pt;
}

/* Control: form. */

#form ol {
	margin: 0;
	padding: 0 5px;
}
#form ol li {
	display: inline;
}
label {
	text-align: left;
	clear: both;
	float: left;
	width: auto;
	margin: 1px 0 0 1px;
	padding: 2px 0;
}
label:after {
	content: ':';
}
input, select {
	color: #000000;
	background-color: #EAEAEA;
	border: 0;
}
.input {
	text-align: right;
}
.input input, .input select {
	border: 1px solid #CCCCCC;
	float: right;
	width: 60%;
	margin: 1px 0 0 2px;
}
input[disabled] {
	color: #666666;
}

/* Control: form: control. */

.control {
	text-align: right;
	margin: 3px;
	padding: 0 0 0 2px;
}
.load .control {
	background-image: url('/styles/normal.gif');
	background-position: left center;
	background-repeat: no-repeat;
}
.active .control {
	background-image: url('/styles/load.gif');
}
#refresh {
	color: #999999;
	float: left;
	padding: 1px;
}
.load #refresh {
	padding-left: 13px;
}
#options {
	width: 1.6em;
	padding: 0;
}

/* Contents. */

#contents {
	border: 1px solid #CCCCCC;
}
#preview {
	text-align: left;
	background-color: #F6F6F6;
	border: 1px solid #CCCCCC;
	display: block;
	margin: 5px;
	padding: 2px;
	cursor: text;
}
#preview:before, #preview:after {
	content: '';
}

/* Contents: Messages. */

#messages li {
	text-align: left;
	background-color: #F6F6F6;
	list-style-type: none;
	margin: 0 0 2px 0;
	padding: 5px;
}
#messages cite {
	font-style: normal;
	font-weight: bold;
	text-align: left;
}
#messages cite:after {
	content: ':';
}
#messages cite a {
	text-decoration: underline;
}
#messages q {
	text-align: left;
	padding: 0;
}
#messages q:before, #messages q:after {
	content: '';
}
#messages q a {
	text-decoration: underline;
}
#messages q a:before {
	content: '[';
}
#messages q a:after {
	content: ']';
}
#messages .option {
	font-size: 7pt;
	text-transform: capitalize;
	color: #999999;
}
#messages dl {
	font-size: 7pt;
	text-align: right;
	color: #999999;
	margin: 2px 0 0 0;
}
#messages dd {
	display: inline;
	margin: 0;
	padding: 0;
}
#messages dd.status {
	cursor: help;
}
#messages .online dd.status, #messages .ip dd.status {
	font-weight: bold;
	color: #80BC00;
}
#messages .admin cite {
	border-bottom: 1px dotted #80BC00;
}
#messages li.admin dl {
	border-left: 3px solid #80BC00;
}

/* Contents: Smileys. */

#smileys {
	margin: 5px 0 0 0;
	padding: 0 3px;
}
#smileys li {
	display: inline;
	padding: 3px;
}
#smileys img {
	cursor: pointer;
}
#smileys code {
	display: none;
}
#smileys.full li {
	text-align: center;
	list-style-type: none;
	float: left;
	width: 40px;
	height: 40px;
	margin: 0;
	padding: 2px 0;
	overflow: hidden;
}
#smileys.full code {
	font-size: 7pt;
	display: block;
	margin: 0;
}

/* Contents: Navigation and paging. */

#navigation, #paging {
	font-size: 7pt;
	clear: both;
	margin: 0;
	padding: 5px;
	overflow: hidden;
}
#navigation dd, #paging dd {
	margin: 0;
	padding: 0;
}
#navigation dd {
	background-color: #F6F6F6;
	margin: 2px 0;
	padding: 3px 0;
}
#navigation strong, #paging strong {
	background-color: #F6F6F6;
}

/* Contents: Notice. */

#notice {
	text-align: left;
	padding: 5px;
}
#notice p {
	margin-bottom: 10px;
}
#notice p a {
	text-decoration: underline;
}

/* Contents: Online list. */

#online {
	text-align: left;
	padding: 5px;
}
#online ul {
	margin: 5px 0 10px 0;
}
#online ul li {
	list-style-type: square;
	list-style-position: inside;
}
#online p {
	font-size: 7pt;
	background-color: #F6F6F6;
	padding: 3px;
}
#online span {
	cursor: help;
}


/* IE only: bad stuff. */

html {
	scrollbar-arrow-color: #333333;
	scrollbar-base-color: #FFFFFF;
	scrollbar-face-color: #F6F6F6;
	scrollbar-shadow-color: #CCCCCC;
	scrollbar-3dlight-color: #CCCCCC;
	scrollbar-darkshadow-color: #FFFFFF;
	scrollbar-highlight-color: #FFFFFF;
	scrollbar-track-color: #FFFFFF;
}
