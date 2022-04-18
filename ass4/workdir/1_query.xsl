<xsl:stylesheet version="1.0" 
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:template match="/">
		<Teams>
			<xsl:for-each select="manufacturingteams/manufacturingteam">
				<xsl:call-template name="team"/>
			</xsl:for-each>
		</Teams>
	</xsl:template>
	<xsl:template name="team">
		<Team>
			<xsl:attribute name="teamid">
				<xsl:value-of select="./manufacturingteamid"/>
			</xsl:attribute>
			<xsl:choose>
				<xsl:when test="./airplanes/airplane">
					<Unit>
						<xsl:attribute name="unitd">
							<xsl:text>Default</xsl:text>
						</xsl:attribute>
						<xsl:attribute name="registration">
							<xsl:value-of select="./airplanes/airplane/@serialNumber"/>
						</xsl:attribute>
						<Wingtips>True</Wingtips>
						<Windows>4</Windows>
						<seatconfig>
							<brand>Recaro</brand>
						</seatconfig>
					</Unit>
				</xsl:when>
				<xsl:otherwise>
					<Units/>
				</xsl:otherwise>
			</xsl:choose>
		</Team>
	</xsl:template>
</xsl:stylesheet>