# Claude Code Skills for jaulgonne-1918

## Historian Skill / Skill Historien

### Quick Start / Démarrage Rapide

The **Historian Skill** is a specialized Claude agent configured for academic historical research and content generation focused on:
- French military and general history
- American military history  
- Military tactics and operations
- The Battle of Jaulgonne and the Second Battle of the Marne (1918)

**Le Skill Historien** est un agent Claude spécialisé configuré pour la recherche historique académique et la génération de contenu axé sur :
- L'histoire militaire et générale de France
- L'histoire militaire américaine
- Les tactiques et opérations militaires
- La Bataille de Jaulgonne et la Deuxième Bataille de la Marne (1918)

### How to Use This Skill / Comment Utiliser Ce Skill

#### In Claude Code CLI / Dans Claude Code CLI

```bash
# Use the historian skill for content generation
claude ask --skill historian "Describe the strategic significance of the Second Battle of the Marne"
```

#### In Custom Instructions / Dans Les Instructions Personnalisées

Reference the historian skill in your Claude Code configuration:

```json
{
  "skills": ["historian"],
  "context": "Generating historical content for the jaulgonne-1918 website"
}
```

### Features / Caractéristiques

✓ **Bilingual Support**: Full English and French proficiency  
✓ **Bilinguisme** : Pleine compétence en anglais et français

✓ **Academic Rigor**: Evidence-based historical analysis  
✓ **Rigueur Académique** : Analyse historique fondée sur des preuves

✓ **Specialization**: Deep expertise in French and American military history  
✓ **Spécialisation** : Expertise approfondie en histoire militaire française et américaine

✓ **Primary Source Integration**: References archives, photographs, and documents  
✓ **Intégration des Sources Primaires** : Références archives, photographies et documents

✓ **Web-Ready Output**: Content formatted for website publication  
✓ **Contenu Prêt pour le Web** : Contenu formaté pour la publication sur le site

### Use Cases / Cas d'Usage

1. **Generate Historical Articles**
   - Battle narratives and timelines
   - Commander biographies
   - Unit histories and operations

2. **Fact-Checking & Verification**
   - Verify historical claims
   - Cross-reference sources
   - Identify historiographical debates

3. **Content Enhancement**
   - Add context to photographs
   - Develop captions with historical details
   - Create educational materials

4. **Research Support**
   - Analyze primary documents
   - Compare historical interpretations
   - Provide academic citations

### Configuration / Configuration

**File**: `historian.md`  
**Version**: 1.0  
**Status**: Active  
**Languages**: English / Français  

### Integration with jaulgonne-1918

This skill leverages the website's research materials:
- **selection_sources/**: Archival photographs and documents
- **Combat units**: American 3rd Division, French forces
- **Time period**: 1918, World War I

### Example Prompts / Exemples de Requêtes

**English:**
> "Based on the Battle of Jaulgonne collection, create a historical narrative of the American 3rd Division's advance on July 18-22, 1918. Include tactical decisions, casualty figures, and relevant primary sources."

**Français:**
> "Basé sur la collection de la Bataille de Jaulgonne, créez un récit historique de l'avancée de la 3ème Division américaine du 18-22 juillet 1918. Incluez les décisions tactiques, les chiffres de pertes et les sources primaires pertinentes."

---

## Implementation Notes / Notes d'Implémentation

- **Single Skill Repository**: All historian-related functionality consolidated in one skill
- **Bilingual by Design**: Both languages are equally supported in all content
- **Website-Focused**: Content generation optimized for web publication
- **Academic Standards**: All historical claims backed by scholarly sources

## Future Enhancements / Améliorations Futures

- Integration with specific document OCR system
- Enhanced photograph metadata and indexing
- Timeline visualization generation
- Multi-perspective historical comparison tools
