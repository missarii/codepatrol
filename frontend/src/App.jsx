import React, { useState } from "react";
import CodeInput from "./CodeInput";
import ResultPage from "./ResultPage";

function App() {
  const [result, setResult] = useState(null);

  return (
    <div className="min-h-screen bg-gray-50">
      {result ? (
