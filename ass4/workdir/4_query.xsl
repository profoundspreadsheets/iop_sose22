<xsl:stylesheet version="1.0" 
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:template match="/">
		<xsl:element name="Planes">
			<xsl:apply-templates select="//airplanes"/>
		</xsl:element>
	</xsl:template>
	<xsl:template match="airplane">
		<xsl:element name="Plane">
			<xsl:attribute name="registration">
				<xsl:value-of select="./serialnumber"/>
			</xsl:attribute>
			<xsl:element name="Color">White</xsl:element>
            <xsl:element name="Livery">eurowhite</xsl:element>
			<xsl:element name="Bars"/>
		</xsl:element>
	</xsl:template>
</xsl:stylesheet>