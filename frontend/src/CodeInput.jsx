import React, { useState } from "react";
import CodeMirror from "@uiw/react-codemirror";
import { javascript } from "@codemirror/lang-javascript";
import { submitCode } from "./api";

export default function CodeInput({ onResult }) {
  const [code, setCode] = useState("// Write your code here");
  const [username, setUsername] = useState("student1");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    try {
      setLoading(true);
      const result = await submitCode(username, code);
      onResult(result);
    } catch (err) {
      alert("Error: " + err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-6 max-w-3xl mx-auto space-y-4">
      <h1 className="text-2xl font-bold">🛡️ CodePatrol – Submit Code</h1>
      <input
        type="text"
        placeholder="Your username"
        className="w-full px-4 py-2 border rounded"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <CodeMirror
        value={code}
        height="300px"
        extensions={[javascript()]}
        onChange={(val) => setCode(val)}
      />
      <button
        onClick={handleSubmit}
        disabled={loading}
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
