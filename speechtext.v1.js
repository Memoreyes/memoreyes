'use strict';

// This example takes uncompressed wav audio from the Text to Speech service and plays it through the computer's speakers
// Should work on windows/mac/linux, but linux may require some extra setup first: https://www.npmjs.com/package/speaker

const TextToSpeechV1 = require('watson-developer-cloud/text-to-speech/v1');
const wav = require('wav');
const Speaker = require('speaker');
require('dotenv').load({ silent: true }); // imports environment properties from a .env file if present

const textToSpeech = new TextToSpeechV1(
  {
    username: '2aec254c-8016-480f-a62a-49b1dd9ce532',
    password: 'fPJSUToKj7Du'
  }
);

const reader = new wav.Reader();

// the "format" event gets emitted at the end of the WAVE header
reader.on('format', function(format) {
  // the WAVE header is stripped from the output of the reader
  reader.pipe(new Speaker(format));
});

textToSpeech.synthesize({ text: 'hello from IBM Watson', accept: 'audio/wav' }).pipe(reader);