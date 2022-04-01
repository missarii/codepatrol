import React, { useState } from "react";
import CodeMirror from "@uiw/react-codemirror";
import { javascript } from "@codemirror/lang-javascript";
import { submitCode } from "./api";

export default function CodeInput({ onResult }) {
  const [code, setCode] = useState("// Write your code here");
