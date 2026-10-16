"""Schémas jsonschema des structures échangées avec l'IA (§4.3)."""
from __future__ import annotations

XY = {"type": "array", "items": {"type": "number"}, "minItems": 2, "maxItems": 2}
CONF = {"type": "number", "minimum": 0, "maximum": 1}

ELEMENT_MUR = {
    "type": "object",
    "required": ["id", "debut", "fin", "epaisseur"],
    "properties": {
        "id": {"type": "string"},
        "debut": XY, "fin": XY,
        "epaisseur": {"type": "number", "minimum": 0.05, "maximum": 1.0},
        "materiau_presume": {"type": "string"},
        "niveaux": {"type": "array", "items": {"type": "integer"}},
        "confiance": CONF,
    },
}

INTERPRETATION_SCHEMA = {
    "type": "object",
    "required": ["batiment", "murs_porteurs", "ouvertures"],
    "properties": {
        "batiment": {
            "type": "object",
            "required": ["niveaux", "emprise"],
            "properties": {
                "niveaux": {"type": "integer", "minimum": 1, "maximum": 40},
                "hauteur_etage": {"type": "number", "minimum": 1.5, "maximum": 8},
                "emprise": {
                    "type": "object",
                    "required": ["largeur", "profondeur"],
                    "properties": {
                        "largeur": {"type": "number", "minimum": 0.5},
                        "profondeur": {"type": "number", "minimum": 0.5},
                    },
                },
                "surface_plancher": {"type": "number", "minimum": 0},
            },
        },
        "murs_porteurs": {"type": "array", "items": ELEMENT_MUR},
        "murs_non_porteurs": {"type": "array", "items": ELEMENT_MUR},
        "ouvertures": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["id", "type", "largeur"],
                "properties": {
                    "id": {"type": "string"},
                    "type": {"type": "string"},
                    "mur": {"type": "string"},
                    "position": {"type": "number"},
                    "largeur": {"type": "number", "minimum": 0},
                    "hauteur": {"type": "number", "minimum": 0},
                    "allege": {"type": "number", "minimum": 0},
                    "confiance": CONF,
                },
            },
        },
        "zones_humides": {"type": "array"},
        "escaliers": {"type": "array"},
        "hypotheses": {"type": "array", "items": {"type": "string"}},
        "incertitudes": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["id", "description", "impact"],
                "properties": {
                    "id": {"type": "string"},
                    "description": {"type": "string"},
                    "impact": {"type": "string"},
                    "suggestion": {"type": "string"},
                },
            },
        },
    },
}

VALIDATION_BLOCK = {
    "type": "object",
    "required": ["statut"],
    "properties": {
        "date": {"type": "string"},
        "statut": {"type": "string", "enum": ["validee", "partiellement_validee", "rejetee"]},
        "corrections": {"type": "array", "items": {
            "type": "object", "required": ["type", "element"],
            "properties": {
                "type": {"type": "string"},
                "element": {"type": "string"},
                "champ": {"type": "string"},
                "avant": {}, "apres": {},
                "raison": {"type": "string"},
            }}},
        "incertitudes_traitees": {"type": "array"},
    },
}
