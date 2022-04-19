<xsl:stylesheet version="1.0" 
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:template match="/">
        <Customers>
            <xsl:apply-templates select="//customers"/>
        </Customers>
    </xsl:template>
	<xsl:template match="customers">
        <xsl:choose>
            <xsl:when test="./customer"> <!-- custmer exists -->
                <Customer>
                    <xsl:attribute name="customerid">
                        <xsl:value-of select="./customer/@customerId"/>
                    </xsl:attribute>
                    <xsl:element name="Firstname">
                        <xsl:value-of select="./customer/firstname"/>
                    </xsl:element>
                    <xsl:element name="Lastname">
                        <xsl:value-of select="./customer/lastname"/>
                    </xsl:element>
                    <xsl:element name="Planes"/>
                </Customer>
            </xsl:when>
            <xsl:otherwise></xsl:otherwise>
        </xsl:choose>
	</xsl:template>
</xsl:stylesheet>