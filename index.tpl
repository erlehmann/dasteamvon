<!DOCTYPE html>
<meta charset=utf-8>
<title>Hier twittert das Team von {{name}}</title>
<style>
  html { font-family: sans-serif; line-height: 1.5; }
  body { margin: 3em auto; max-width: 33em; }
  body > *, form > label, form > input { display: block; width: 100%; }
  label > input { float: right; width: 50%; }
  form > * { margin: 0.75em 0; }
  input[type=submit] { padding: 0.75em; }
</style>
<h1>Hier twittert das Team von {{name}}</h1>
% if statuses:
<ul>
% for s in statuses:
  <li><a href="http://twitter.com/home?status={{quote(s)}}">{{s}}</a>
% end
</ul>
% end
<form method=get>
% for v in variables:
  <label for={{v}}>
    {{v.capitalize()}}
    <input name={{v}} list={{v}}>
  </label>
  <datalist id={{v}}>
%   for o in variables[v]:
    <option value="{{o.strip()}}">
%   end
  </datalist>
% end
  <input type=submit value='GAGA, GOGO, TRALAFITTI'>
</form>
