<<<<<<< HEAD
'use strict';

const TextToSpeechV1 = require('watson-developer-cloud/text-to-speech/v1');
const fs = require('fs');

var contents = fs.readFileSync('DATA.txt', 'utf8');

const textToSpeech = new TextToSpeechV1(
  {
    username: '2aec254c-8016-480f-a62a-49b1dd9ce532',
    password: 'fPJSUToKj7Du'
  }
);

// Synthesize speech and then pipe the results to a file
textToSpeech
  .synthesize({
    text: contents,
    voice: 'en-US_AllisonVoice', // Optional voice
    accept: 'audio/wav' // default is audio/ogg; codec=opus
  })
  .pipe(fs.createWriteStream('output.wav'));

// Retrieve details of all available voices
textToSpeech.voices({}, function(err, res) {
  if (err) {
    return console.log(err);
  }
  //console.log(JSON.stringify(res, null, 2));
});

// Retrieve details of a specific voice
textToSpeech.voice(
  {
    voice: 'en-GB_KateVoice'
  }
  // function(err, res) {
  //   if (err) {
  //     return console.log(err);
  //   }
  //   //console.log(JSON.stringify(res, null, 2));
  // }
);

// Pronunciation details for a word
textToSpeech.pronunciation(
  {
    text: 'iPhone',
    format: 'spr', // 'ipa' (default) is only for english voices
    voice: 'de-DE_DieterVoice' // optional, defaults to en-US_MichaelVoice
  }
 // function(err, res) {
   // if (err) {
    //  return console.log(err);
    //}
    //console.log(JSON.stringify(res, null, 2));
  //}
);
=======
'use strict';

const TextToSpeechV1 = require('watson-developer-cloud/text-to-speech/v1');
const fs = require('fs');

var contents = fs.readFileSync('DATA.txt', 'utf8');

const textToSpeech = new TextToSpeechV1(
  {
    username: '2aec254c-8016-480f-a62a-49b1dd9ce532',
    password: 'fPJSUToKj7Du'
  }
);

// Synthesize speech and then pipe the results to a file
textToSpeech
  .synthesize({
    text: contents,
    voice:  "en-US_AllisonVoice", // Optional voice
    accept: 'audio/wav' // default is audio/ogg; codec=opus
  })
  .pipe(fs.createWriteStream('output.wav'));

// Retrieve details of all available voices
textToSpeech.voices({}, function(err, res) {
  if (err) {
    return console.log(err);
  }
  console.log(JSON.stringify(res, null, 2));
});

// Retrieve details of a specific voice
textToSpeech.voice(
  {
    voice: 'en-GB_KateVoice'
  },
  function(err, res) {
    if (err) {
      return console.log(err);
    }
    console.log(JSON.stringify(res, null, 2));
  }
);

// Pronunciation details for a word
textToSpeech.pronunciation(
  {
    text: 'iPhone',
    format: 'spr', // 'ipa' (default) is only for english voices
    voice: 'de-DE_DieterVoice' // optional, defaults to en-US_MichaelVoice
  },
 function(err, res) {
   if (err) {
     return console.log(err);
    }
    console.log(JSON.stringify(res, null, 2));
  }
);
>>>>>>> 5683b17082af3af3b4b50f4e2ae32fadd0cde26b
