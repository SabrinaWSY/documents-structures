declare function local:determine_frequency($words as xs:string*) as element(word)*{
  for $word in fn:distinct-values($words)
  let $item := 
  element word {
    attribute frequency {fn:count ($words[.=$word])},
    $word
  }
  order by $item/@frequency descending
  return $item
};
let $data := 
<li id="footer-info-lastmod"> You are looking at the page of Wikibooks. This page was last edited on 4 February 2019, at 18:01.</li>
let $sentence := $data/text()
return local:determine_frequency($sentence)