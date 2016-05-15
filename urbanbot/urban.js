var Nightmare = require('nightmare');
var nightmare = Nightmare({ show: true })

nightmare
  .goto('http://urbandictionary.com/define.php?term=klaas')
  .click('html.wf-sourcesanspro-n4-active.wf-sourcesanspro-n6-active.wf-sourcesanspro-n7-active.wf-sourcesanspro-n9-active.wf-lora-n7-active.wf-active body.define_controller div#ud-root div#outer div.three-columns div.row div.small-12.large-8.columns div#content div.def-panel div.def-footer div.row div.columns div.left.thumbs div.thumbs a.up span.count')
  .click('html.wf-sourcesanspro-n4-active.wf-sourcesanspro-n6-active.wf-sourcesanspro-n7-active.wf-sourcesanspro-n9-active.wf-lora-n7-active.wf-active body.define_controller div#ud-root div#outer div.three-columns div.row div.small-12.large-8.columns div#content div.def-panel div.def-footer div.row div.columns div.left.thumbs div.thumbs a.down')
  .click('html.wf-sourcesanspro-n4-active.wf-sourcesanspro-n6-active.wf-sourcesanspro-n7-active.wf-sourcesanspro-n9-active.wf-lora-n7-active.wf-active body.define_controller div#ud-root div#outer div.three-columns div.row div.small-12.large-8.columns div#content div.def-panel div.def-footer div.row div.columns div.left.thumbs div.thumbs a.down span.count')
  .evaluate(function () {
    return 0
  })
  .end()
  .then(function (result) {
    console.log(result)
  })
  .catch(function (error) {
    console.error('Search failed:', error);
  });
