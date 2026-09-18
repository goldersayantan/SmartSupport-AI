import "./ExampleTickets.css";

function ExampleTickets({ onSelect }) {
  const exampleTickets = [
    "My package has been delayed for three days",
    "Someone used my account and I cannot log in",
    "My payment failed but money was deducted",
    "I want to change my email address",
  ];

  return (
    <section className="example-tickets">

      <div className="example-heading">
        <span>💡</span>

        <div>
          <strong>Try an example</strong>
          <p>
            Click an example to quickly test the AI.
          </p>
        </div>
      </div>

      <div className="example-list">
        {exampleTickets.map((example, index) => (
          <button
            key={index}
            type="button"
            className="example-ticket-button"
            onClick={() => onSelect(example)}
          >
            <span>→</span>
            {example}
          </button>
        ))}
      </div>

    </section>
  );
}

export default ExampleTickets;
