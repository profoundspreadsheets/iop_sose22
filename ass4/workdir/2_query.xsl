<xsl:stylesheet version="1.0" 
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:template match="/">
		<xsl:element name="Customers">
			<xsl:apply-templates select="//customers"/>
		</xsl:element>
	</xsl:template>
	<xsl:template match="customers">
		<xsl:choose>
			<xsl:when test="./customer">
				<!-- customer exists -->
				<Customer>
					<xsl:attribute name="customerid">
						<xsl:value-of select="./customer/@customerId"/>
					</xsl:attribute>
					<xsl:element name="Firstname">
						<xsl:value-of select="./customer/firstname"/>
					</xsl:element>
					<xsl:element name="Lastname">
						<xsl:value-of select="./customer/surname"/>
					</xsl:element>
					<xsl:element name="Planes">
						<xsl:choose>
							<xsl:when test="./customer/specification/specification">
								<!-- specification exists, registration mapped to specificationid-->
								<xsl:element name="Plane">
									<xsl:attribute name="registration">
										<xsl:value-of select="./customer/specification/specification/@specificationId"/>
									</xsl:attribute>
									<xsl:element name="Protocols"></xsl:element>
								</xsl:element>
							</xsl:when>
						</xsl:choose>
					</xsl:element>
				</Customer>
			</xsl:when>
		</xsl:choose>
	</xsl:template>
</xsl:stylesheet>