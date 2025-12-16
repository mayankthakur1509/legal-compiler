export default function AuthorityPage({ lawyer }) {
  return (
    <div>
      <h1>{lawyer.name}</h1>
      <p>{lawyer.role}</p>
    </div>
  );
}
