<xsl:stylesheet version="1.0" 
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:template match="/">
		<!-- using 2_data.xml -->
		<xsl:element name="Teams">
			<xsl:for-each select="manufacturingteams/manufacturingteam">
				<xsl:call-template name="team"/>
			</xsl:for-each>
		</xsl:element>
	</xsl:template>
	<xsl:template name="team">
		<xsl:element name="Team">
			<xsl:attribute name="teamid">
				<xsl:value-of select="./manufacturingteamid"/>
			</xsl:attribute>
			<xsl:attribute name="employees">
				<xsl:value-of select="./manufacturingteamaddress/address/address/street/number[./@type='staircase']"/>
			</xsl:attribute>
			<xsl:element name="Units">
				<xsl:choose>
					<xsl:when test="./airplanes/airplane">
						<!-- airplane exists-->
						<xsl:element name="Unit">
							<xsl:attribute name="unitid">
								<xsl:variable name="teamname" select="./manufacturingteamname"/>
								<xsl:variable name="teamcity" select="./manufacturingteamaddress/address/address/city"/>
								<xsl:value-of select="$teamname"/>
								<xsl:value-of select="$teamcity"/>
							</xsl:attribute>
							<xsl:attribute name="registration">
								<xsl:value-of select="./airplanes/airplane/@serialNumber"/>
							</xsl:attribute>
							<xsl:element name="Wingtips">
								<xsl:choose>
									<!-- model element unusable because mix of int and string so i compare serialnumber -->
									<xsl:when test="number(./airplanes/airplane/@serialNumber) &gt; 500">True</xsl:when>
									<xsl:otherwise>False</xsl:otherwise>
								</xsl:choose>
							</xsl:element>
							<xsl:element name="Windows">4</xsl:element>
							<xsl:element name="seatconfig">
								<xsl:element name="brand">Recaro</xsl:element>
							</xsl:element>
						</xsl:element>
					</xsl:when>
					<xsl:otherwise>
						<!-- no airplane, so no data really useful-->
						<xsl:element name="Unit">
							<xsl:attribute name="unitid">
								<xsl:variable name="teamname" select="./manufacturingteamname"/>
								<xsl:variable name="teamcity" select="./manufacturingteamaddress/address/address/city"/>
								<xsl:value-of select="$teamname"/>
								<xsl:value-of select="$teamcity"/>
							</xsl:attribute>
							<xsl:attribute name="registration">
								<xsl:text>No plane</xsl:text>
							</xsl:attribute>
							<xsl:element name="seatconfig">
								<xsl:element name="brand">Recaro</xsl:element>
							</xsl:element>
						</xsl:element>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:element>
		</xsl:element>
	</xsl:template>
</xsl:stylesheet>