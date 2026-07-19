import { useState, useEffect } from "react";

const steps = [
  "Reading your resume",
  "Researching the company",
  "Finding relevant news",
  "Writing your email",
];

function Spinner() {
  const [activeStep, setActiveStep] = useState(0);

  useEffect(() => {
    if (activeStep >= steps.length - 1) return;

    const timer = setTimeout(() => {
      setActiveStep((prev) => prev + 1);
    }, 2000);

    return () => clearTimeout(timer);
  }, [activeStep]);

  return (
    <div className="spinner">
      {steps.map((step, i) => (
        <div
          key={i}
          className={`spinner-step ${i < activeStep ? "done" : ""} ${i === activeStep ? "active" : ""}`}
        >
          <span className="spinner-dot" />
          <span>{step}</span>
        </div>
      ))}
    </div>
  );
}

export default Spinner;