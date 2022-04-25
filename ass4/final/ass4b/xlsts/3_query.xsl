<xsl:stylesheet version="1.0" 
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:template match="/">
		<!-- using 4_data.xml -->
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
					<xsl:choose>
						<xsl:when test="./companies/company[1]">
							<xsl:attribute name="unitid">
								<xsl:value-of select="./companies/company[1]/companyname"/>
								<xsl:value-of select="./companies/company[1]/@companyId"/>
							</xsl:attribute>
							<xsl:element name="Capacity">
								<xsl:value-of select="number(./companies/company[1]/@companyId div 80)"/>
							</xsl:element>
							<xsl:element name="Flowrate">
								<xsl:value-of select="number(./companies/company[1]/@companyId div 320)"/>
							</xsl:element>
						</xsl:when>
						<xsl:otherwise>
							<xsl:attribute name="unitid">UUID</xsl:attribute>
							<xsl:element name="Capacity">2.0</xsl:element>
							<xsl:element name="Flowrate">10.0</xsl:element>
						</xsl:otherwise>
					</xsl:choose>
				</xsl:element>
			</xsl:element>
		</xsl:element>
	</xsl:template>
</xsl:stylesheet>