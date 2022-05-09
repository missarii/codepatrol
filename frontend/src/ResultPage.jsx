import React from "react";

export default function ResultPage({ result, onBack }) {
  return (
    <div className="p-6 max-w-xl mx-auto space-y-6 text-center">
      <h2 className="text-2xl font-semibold">🧠 Results</h2>
      <p className="text-lg">
        🔍 <span className="font-medium">Similarity Score:</span> {result.score}%
      </p>
      {result.match && (
        <p className="text-lg text-gray-700">
          🧑 Match Found With: <span className="font-bold">{result.match}</span>
        </p>
      )}
      {!result.match && <p className="text-gray-500">✅ No matching submission found.</p>}
      <button
        onClick={onBack}
        className="mt-4 bg-gray-700 text-white px-4 py-2 rounded hover:bg-gray-800"
      >
        ← Submit Another
