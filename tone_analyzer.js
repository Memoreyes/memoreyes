
var ToneAnalyzerV3 = require('watson-developer-cloud/tone-analyzer/v3')
var tone_analyzer = new ToneAnalyzerV3 ({
    username: '02df825b-ce61-4d58-86d1-a4303c019896',
    password: '5KRmWrcYEqYV',
    version_date: '2016-05-19'
});

var params = {
  // Get the text from the JSON file.
  text: 'I am very mad',//require('tone.json').text,
  tones: 'emotion'
};

tone_analyzer.tone(params, function(error, response) {
  if (error)
    console.log('error:', error);
  else
    console.log(JSON.stringify(response, null, 2));
  }
);
