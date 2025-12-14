from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig

class PIIScrubber:
    def __init__(self):
        """
        Initialize the PII Scrubber with Presidio Analyzer and Anonymizer engines
        Done once on startup for efficiency.
        """
        self.analyzer = AnalyzerEngine()
        self.anonymizer = AnonymizerEngine()

        # Define relevant PII entity types
        self.entities = [
            "PERSON",
            "EMAIL_ADDRESS",
            "PHONE_NUMBER",
            "CREDIT_CARD",
            "US_SSN",
            "LOCATION",
            "DATE_TIME",
            "IP_ADDRESS",
            "URL"
        ]

    def scrub_text(self, text: str) -> str:
        """
        Scrub PII from the provided text.
        """

        # Analyze the text to find PII entities
        results = self.analyzer.analyze(
            text=text,
            entities=self.entities,
            language="en"
        )

        # Anonymize the detected PII entities
        anonymizer_result = self.anonymizer.anonymize(
            text=text,
            analyzer_results=results,
            operators={
                "default": OperatorConfig("replace", {"new_value": "[REDACTED-{entity_type}>]"})
            }
        )

        # Return the scrubbed text and details of redacted items
        return {
            "clean_text": anonymizer_result.text,
            "redacted_items": [res.entity_type for res in results]
        }

# Instantiate the PII Scrubber service
scrubber_service = PIIScrubber()
