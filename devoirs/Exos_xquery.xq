declare function local:sp_sen($sentence as xs:string){
  tokenize($sentence, '\.')
};
declare function local:word-count( $sentence as xs:string? ) as xs:integer {
  count(tokenize($sentence, '\W+')[. != ''])
};

let $data := 
<li id="footer-info-lastmod"> You are looking at the page of Wikibooks. This page was last edited on 4 February 2019, at 18:01.</li>
let $sentence := $data/text()
return local:word-count($sentence)