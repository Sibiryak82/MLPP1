# ������ 1.33.PP4E\Preview\peoplecqi.html
import cqi, shelve, sys, os, html

<html>
<title>People Input Form</title>
<body>
<form method=POST action="cqi-bin/peoplecqi.py">
<table>
<tr><th>Key <td><input type=text name=key>
<tr><th>Name<td><input type=text name=name>
<tr><th>Age <td><input type=text name=age>
<tr><th>Job <td><input type=text name=job>
<tr><th>Pay <td><input type=text name=pay>
</table>
<p>
<input type=submit value="Fetch", name=action>
<input type=submit value="Update", name=action>
</form>
</body></html>