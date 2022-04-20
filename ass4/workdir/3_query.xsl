<xsl:stylesheet version="1.0" 
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:template match="/">
		<xsl:element name="Planes">
			<xsl:apply-templates select="//customers"/>
		</xsl:element>
	</xsl:template>
	<xsl:template match="customer">
		<xsl:element name="Plane">
			<xsl:attribute name="registration">
				<xsl:value-of select="./customerid"/>
			</xsl:attribute>
			<xsl:element name="Customer">
				<xsl:element name="Firstname">
					<xsl:value-of select="./firstname"/>
				</xsl:element>
				<xsl:element name="Lastname">
					<xsl:value-of select="./surname"/>
				</xsl:element>
			</xsl:element>
			<xsl:element name="Toilets">
				<xsl:element name="ToiletSpecs">
					<xsl:attribute name="unitid">UUID</xsl:attribute>
					<xsl:element name="Capacity">2.0</xsl:element>
					<xsl:element name="Flowrate">10.0</xsl:element>
				</xsl:element>
			</xsl:element>
		</xsl:element>
	</xsl:template>
</xsl:stylesheet>