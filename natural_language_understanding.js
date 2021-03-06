
 var NaturalLanguageUnderstandingV1 = require('watson-developer-cloud/natural-language-understanding/v1.js');

 var natural_language_understanding = new NaturalLanguageUnderstandingV1 ({
    username: '0707e150-a78d-4e3f-a7c4-95423c1a5e9c',
    password: 'EE5OnIlV2jRC',
    version_date: '2017-02-27'
});

var parameters = {
  'text': 'IBM is an American multinational technology company headquartered in Armonk, New York, United States, with operations in over 170 countries.',
  'features': {
    'entities': {
      'emotion': true,
      'sentiment': true,
      'limit': 2
    },
    'keywords': {
      'emotion': true,
      'sentiment': true,
      'limit': 2
    }
  }
}

natural_language_understanding.analyze(parameters, function(err, response) {
  if (err)
    console.log('error:', err);
  else
    console.log(JSON.stringify(response, null, 2));
});