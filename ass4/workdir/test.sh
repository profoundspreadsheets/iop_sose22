# tested on my macheine with saxon 10.6, as it was only package available on AUR, sorry
# all files must be in same directory, as given per assignment!
echo ".xq queries"
java -cp /home/paul/Downloads/saxon-he/src/saxon-he-10.6.jar net.sf.saxon.Query -q:1_query.xq -o:1_output.xml
xmllint --noout --relaxng 1_schema.rng 1_output.xml
java -cp /home/paul/Downloads/saxon-he/src/saxon-he-10.6.jar net.sf.saxon.Query -q:2_query.xq -o:2_output.xml
xmllint --noout --relaxng 2_schema.rng 2_output.xml
java -cp /home/paul/Downloads/saxon-he/src/saxon-he-10.6.jar net.sf.saxon.Query -q:3_query.xq -o:3_output.xml
xmllint --noout --relaxng 3_schema.rng 3_output.xml
java -cp /home/paul/Downloads/saxon-he/src/saxon-he-10.6.jar net.sf.saxon.Query -q:4_query.xq -o:4_output.xml
xmllint --noout --relaxng 4_schema.rng 4_output.xml

echo ".xsl queries"
xsltproc 1_query.xsl 2_data.xml > 1_output.xml
xmllint --noout --relaxng 1_schema.rng 1_output.xml
xsltproc 2_query.xsl 1_data.xml > 2_output.xml
xmllint --noout --relaxng 2_schema.rng 2_output.xml
xsltproc 3_query.xsl 4_data.xml > 3_output.xml
xmllint --noout --relaxng 3_schema.rng 3_output.xml
xsltproc 4_query.xsl 3_data.xml > 4_output.xml
xmllint --noout --relaxng 4_schema.rng 4_output.xml